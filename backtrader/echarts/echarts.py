#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2020 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
'''
    集成pyecharts
'''


from ..utils.py3 import range, with_metaclass, string_types, integer_types
from .. import AutoInfoClass, MetaParams, TimeFrame, date2num
from ..utils.dateintern import num2date
import numpy as np

class Echarts_Line(with_metaclass(MetaParams, object)):
    def __init__(self, **kwargs):
        pass

    def render(self,strategy):
        if not strategy.datas:
            return

        if not len(strategy):
            return

        from pyecharts import options as opts
        from pyecharts.charts import Kline

        date_time = strategy.lines.datetime.array.tolist()
        x_data = [num2date(date).strftime('%Y-%m-%d') for date in date_time]
        data_open = strategy.data.lines.open.array
        data_high = strategy.data.lines.high.array
        data_low = strategy.data.lines.low.array
        data_close = strategy.data.lines.close.array
        data = [data_open,data_high,data_low,data_close]
        y_data = np.array(data).T.tolist()
        k_line = Kline()
        k_line.add_xaxis(x_data)
        k_line.add_yaxis("kline", y_data)
        k_line.set_global_opts(
            xaxis_opts=opts.AxisOpts(is_scale=True),
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ),
            ),
            datazoom_opts=[opts.DataZoomOpts(pos_bottom="-2%")],
            title_opts=opts.TitleOpts(title="股票数据"),
        )
        k_line.render()


Echarts = Echarts_Line

