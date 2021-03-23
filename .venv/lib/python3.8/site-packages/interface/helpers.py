from collections import defaultdict
from .formatting import bulleted_list
from .functional import item_map
from .typecheck import compatible


def merge_signatures(interfaces):
    """
    Merge signatures from one or more interfaces.

    If multiple interfaces define a signature with the same name, we take the
    one with the most specialized implementation. If any same-named signatures
    are incompatible, a TypeError is raised.

    Parameters
    ----------
    interfaces : tuple[Interface]
        Interfaces to merge.

    Returns
    -------
    merged : dict[str -> inspect.Signature
        Merged signatures.

    See Also
    --------
    :func:`interface.typecheck.compatible`
    """
    all_signatures = defaultdict(list)
    for i in interfaces:
        for name, signature in i._signatures.items():
            all_signatures[name].append((i, signature))

    return item_map(_most_specific_signature, all_signatures)


def _most_specific_signature(name, signatures):
    """
    Parameters
    ----------
    name : str
    signatures : list[(Interface, inspect.Signature)]

    Returns
    -------
    inspect.Signature

    Raises
    ------
    TypeError
    """
    # Assume entry is most specific.
    best_iface, best_sig = signatures[0]

    for candidate_iface, candidate_sig in signatures:
        if compatible(candidate_sig, best_sig):
            # If the new candidate is a refinement of the current best, use it.
            best_iface = candidate_iface
            best_sig = candidate_sig
        elif compatible(best_sig, candidate_sig):
            # If the old candidate is a refinement of the candidate, keep the
            # old candidate.
            continue
        else:
            conflicts = [
                '.'.join([best_iface.__name__, str(best_sig)]),
                '.'.join([candidate_iface.__name__, str(candidate_sig)]),
            ]
            raise TypeError(
                "Incompatible signatures for method {}:\n"
                "{}".format(name, bulleted_list(conflicts))
            )

    return best_sig


def merge_defaults(bases):
    """Merge
    """
