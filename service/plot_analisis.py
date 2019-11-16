"""
Copyright (c) 2018-2019 Vincenzo Palazzo vicenzopalazzodev@gmail.com
Distributed under the Apache License Version 2.0 software license,
see https://www.apache.org/licenses/LICENSE-2.0.txt
"""
import plotly.graph_objects as go
from model.type_script_value import TypescriptValue


class PlotAnalisis:

    def plot(self, data_analisis):
        fig = go.Figure()
        keys = data_analisis.keys()
        p2pk_values = []
        p2pkh_values = []
        p2ms_values = []
        no_standard = []
        op_return = []
        op_p2sh = []
        op_p2wpkh = []
        op_p2wsh = []
        copy_keys = []
        for key in keys:
            copy_keys.append(int(key))
        copy_keys.sort()
        for key in copy_keys:
            value_for_year = data_analisis[key]
            p2pk_values.append(value_for_year.get_data()[TypescriptValue.TYPE_P2PK])
            p2pkh_values.append(value_for_year.get_data()[TypescriptValue.TYPE_P2PKH])
            p2ms_values.append(value_for_year.get_data()[TypescriptValue.TYPE_P2MS])
            no_standard.append(value_for_year.get_data()[TypescriptValue.TYPE_NO_STANDARD])
            op_return.append(value_for_year.get_data()[TypescriptValue.TYPE_OP_RETURN])
            op_p2sh.append(value_for_year.get_data()[TypescriptValue.TYPE_P2SH])
            op_p2wpkh.append(value_for_year.get_data()[TypescriptValue.TYPE_P2WPKH])
            op_p2wsh.append(value_for_year.get_data()[TypescriptValue.TYPE_P2WSH])

        fig.add_trace(go.Scatter(x=copy_keys, y=p2pk_values, mode='lines+markers', name='P2PK',
                                 line_color='rgb(153, 84, 187)'))

        fig.add_trace(go.Scatter(x=copy_keys, y=p2pkh_values, mode='lines+markers', name='P2PKH',
                                 line_color='rgb(39, 128, 227)'))

        fig.add_trace(go.Scatter(x=copy_keys, y=p2ms_values, mode='lines+markers', name='P2MS',
                                 line_color='rgb(255, 0, 57)'))

        fig.add_trace(go.Scatter(x=copy_keys, y=no_standard, mode='lines+markers', name='NO_STANDARD',
                                 line_color='rgb(255, 117, 24)'))

        fig.add_trace(go.Scatter(x=copy_keys, y=op_return, mode='lines+markers', name='OP_RETURN',
                                 line_color='rgb(61, 176, 23)'))

        fig.add_trace(go.Scatter(x=copy_keys, y=op_p2sh, mode='lines+markers', name='P2SH',
                                 line_color='rgb(38, 198, 218)'))

        fig.add_trace(go.Scatter(x=copy_keys, y=op_p2wsh, mode='lines+markers', name='P2WSH',
                                 line_color='rgb(233, 30, 99)'))

        fig.add_trace(go.Scatter(x=copy_keys, y=op_p2wpkh, mode='lines+markers', name='P2WPKH',
                                 line_color='rgb(55, 71, 79)'))

        # Information graph
        fig.update_layout(title='The estimate the type of Script PubKey utilized in the Bitcoin Blockchain',
                          xaxis_title='Year',
                          yaxis_title='Number of occurrences')
        fig.show()
