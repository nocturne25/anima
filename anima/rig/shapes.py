# -*- coding: utf-8 -*-
# Copyright (c) 2012-2014, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

import pymel.core as pm


class Shape(object):
    """Draws predefined controller shapes
    """

    @classmethod
    def rename(cls, node, name):
        if node and name:
            if isinstance(node, list):
                if isinstance(node[1], pm.nt.Cluster):
                    node[1].rename(name)
                else:
                    node[0].rename(name)
            else:
                node.rename(name)

    @classmethod
    def circle(cls, name=''):
        node =  pm.circle(nr=(0, 1, 0), c=(0, 0, 0), sw=360, r=1, ch=0)
        cls.rename(node[0], name)

        return node[0]

    @classmethod
    def arrowCtrl(cls, name=''):
        node = pm.curve(
            per=True,
            d=1,
            p=[
                (-1, 0, 0),
                ( 1, 0, 0),
                ( 1, 3, 0),
                ( 2, 3, 0),
                ( 0, 5, 0),
                (-2, 3, 0),
                (-1, 3, 0),
                (-1, 0, 0)
            ],
            k=([0, 1, 2, 3, 4, 5, 6, 7])
        )
        cls.rename(node, name)
        return node

    @classmethod
    def fourSidedArrowCtrl(cls, name=''):
        node = pm.curve(
            per=True, d=1,
            p=[(-0.31907, 1.758567, 0),
               (-0.31907, 0.272474, 0),
               (-1.758567, 0.272474, 0),
               (-1.758567, 1.172378, 0),
               (-2.930946, 0, 0),
               (-1.758567, -1.172378, 0),
               (-1.758567, -0.272474, 0),
               (-0.31907, -0.272474, 0),
               (-0.31907, -1.758567, 0),
               (-1.172378, -1.758567, 0),
               (0, -2.930946, 0),
               (1.172378, -1.758567, 0),
               (0.31907, -1.758567, 0),
               (0.31907, -0.272474, 0),
               (1.758567, -0.272474, 0),
               (1.758567, -1.172378, 0),
               (2.930946, 0, 0),
               (1.758567, 1.172378, 0),
               (1.7585607, 0.272474, 0),
               (0.31907, 0.272474, 0),
               ( 0.31907, 1.758567, 0),
               (1.172378, 1.758567, 0),
               (0, 2.930946, 0),
               (-1.172378, 1.758567, 0),
               (-0.31907, 1.758567, 0)
            ],
            k=([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                18, 19, 20, 21, 22, 23, 24])
        )
        cls.rename(node, name)
        return node

    @classmethod
    def ikCtrl(cls, name=''):
        node = pm.curve(
            per=True, d=1,
            p=[( 0.552734, 0, -0.138183), ( 0.552734, 0, -0.184245),
               ( 0.552734, 0, -0.230306), ( 0.552734, 0, -0.276367),
               ( 0.644856, 0, -0.184245), ( 0.736978, 0, -0.0921223),
               ( 0.829101, 0, 0),         ( 0.736978, 0, 0.0921223),
               ( 0.644856, 0, 0.184245),  ( 0.552734, 0, 0.276367),
               ( 0.552734, 0, 0.230306),  ( 0.552734, 0, 0.184245),
               ( 0.552734, 0, 0.138183),  ( 0.517927, 0, 0.138183),
               ( 0.48312, 0, 0.138183),   ( 0.448313, 0, 0.138183),
               ( 0.444285, 0, 0.150144),  (0.436622, 0, 0.170644),
               ( 0.419439, 0, 0.209124),  (0.402845, 0, 0.239713),
               ( 0.386952, 0, 0.264852),  ( 0.371754, 0, 0.286013),
               ( 0.359029, 0, 0.301972),  (0.342183, 0, 0.321041),
               ( 0.32585, 0, 0.337618),   (0.305397, 0, 0.356146),
               ( 0.290641, 0, 0.368196),  ( 0.270877, 0, 0.382837),
               ( 0.256838, 0, 0.392304),  (0.233632, 0, 0.406427),
               ( 0.208595, 0, 0.419739),  (0.181267, 0, 0.432208),
               ( 0.158735, 0, 0.440999),  ( 0.138233, 0, 0.447895),
               ( 0.138183, 0, 0.481828),  (0.138183, 0, 0.517281),
               ( 0.138183, 0, 0.552734),  (0.184245, 0, 0.552734),
               ( 0.230306, 0, 0.552734),  ( 0.276367, 0, 0.552734),
               ( 0.184245, 0, 0.644856),  (0.0921223, 0, 0.736978),
               ( 0, 0, 0.829101),         (-0.0921223, 0, 0.736978),
               ( -0.184245, 0, 0.644856), (-0.276367, 0, 0.552734),
               ( -0.230306, 0, 0.552734), (-0.184245, 0, 0.552734),
               ( -0.138183, 0, 0.552734), (-0.138183, 0, 0.517349),
               ( -0.138183, 0, 0.481964), (-0.138183, 0, 0.446579),
               ( -0.157573, 0, 0.440389), (-0.195184, 0, 0.425554),
               ( -0.226251, 0, 0.41026),  (-0.261537, 0, 0.389117),
               ( -0.287101, 0, 0.37091),  (-0.313357, 0, 0.349202),
               ( -0.327368, 0, 0.336149), (-0.344095, 0, 0.318984),
               ( -0.366533, 0, 0.292752), (-0.382675, 0, 0.271108),
               ( -0.404132, 0, 0.237612), (-0.417852, 0, 0.212369),
               ( -0.431433, 0, 0.183106), (-0.441634, 0, 0.156968),
               ( -0.449357, 0, 0.133453), (-0.464563, 0, 0.135341),
               ( -0.489623, 0, 0.137181), ( -0.509494, 0, 0.137868),
               ( -0.526834, 0, 0.138116), ( -0.542441, 0, 0.138179),
               ( -0.552734, 0, 0.138183), ( -0.552734, 0, 0.184245),
               ( -0.552734, 0, 0.230306), ( -0.552734, 0, 0.276367),
               ( -0.644856, 0, 0.184245), ( -0.736978, 0, 0.0921223),
               ( -0.829101, 0, 0),        ( -0.736978, 0, -0.0921223),
               ( -0.644856, 0, -0.184245), ( -0.552734, 0, -0.276367),
               ( -0.552734, 0, -0.230306), ( -0.552734, 0, -0.184245),
               ( -0.552734, 0, -0.138183), ( -0.518383, 0, -0.138183),
               ( -0.484033, 0, -0.138183), ( -0.448148, 0, -0.137417),
               ( -0.438965, 0, -0.164253), ( -0.430847, 0, -0.184482),
               ( -0.420951, 0, -0.206126), ( -0.412191, 0, -0.223225),
               ( -0.395996, 0, -0.251053), ( -0.388009, 0, -0.263343),
               ( -0.36993, 0, -0.288412),  ( -0.352908, 0, -0.309157),
               ( -0.331158, 0, -0.33242),  ( -0.311574, 0, -0.350787),
               ( -0.287785, 0, -0.370404), ( -0.266573, 0, -0.385789),
               ( -0.242718, 0, -0.401044), ( -0.216381, 0, -0.41566),
               ( -0.190836, 0, -0.427831), ( -0.163247, 0, -0.438946),
               ( -0.149238, 0, -0.443829), ( -0.138183, 0, -0.447335),
               ( -0.138183, 0, -0.482468), ( -0.138183, 0, -0.517601),
               ( -0.138183, 0, -0.552734), ( -0.184245, 0, -0.552734),
               ( -0.230306, 0, -0.552734), ( -0.276367, 0, -0.552734),
               ( -0.184245, 0, -0.644856), ( -0.0921223, 0, -0.736978),
               ( 0, 0, -0.829101),         ( 0.0921223, 0, -0.736978),
               ( 0.184245, 0, -0.644856), ( 0.276367, 0, -0.552734),
               ( 0.230306, 0, -0.552734), ( 0.184245, 0, -0.552734),
               ( 0.138183, 0, -0.552734), ( 0.138183, 0, -0.517258),
               ( 0.138183, 0, -0.481783), ( 0.138183, 0, -0.446308),
               ( 0.168167, 0, -0.436473), ( 0.190718, 0, -0.427463),
               ( 0.207556, 0, -0.419785), ( 0.22845, 0, -0.409061),
               ( 0.259644, 0, -0.39037),  ( 0.28708, 0, -0.37093),
               ( 0.309495, 0, -0.352609), ( 0.341156, 0, -0.322135),
               ( 0.358246, 0, -0.302914), ( 0.375889, 0, -0.280529),
               ( 0.387391, 0, -0.26426),  ( 0.402652, 0, -0.240132),
               ( 0.411495, 0, -0.224515), ( 0.423963, 0, -0.199829),
               ( 0.430266, 0, -0.185834), ( 0.437317, 0, -0.16858),
               ( 0.444059, 0, -0.150009), ( 0.447312, 0, -0.14009),
               ( 0.480289, 0, -0.138183), ( 0.516511, 0, -0.138183),
               ( 0.552734, 0, -0.138183)],
            k=([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
                34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65,
                66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
                82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,
                98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122,
                123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134,
                135, 136, 137, 138, 139, 140, 141, 142, 143, 144]
            )
        )
        cls.rename(node, name)
        return node

    @classmethod
    def bodyCtrl(cls, name=''):
        node = pm.curve(
            per=True, d=1,
            p=[
                ( -1, 0, 1), ( -1, 0, -1), ( 1, 0, -1), ( 1, 0, 1), ( -1, 0, 1)
            ],
            k=[0, 1, 2, 3, 4]
        )
        cls.rename(node, name)
        return node

    @classmethod
    def elbowCtrl(cls, name=''):
        node = pm.curve(
            d=3,
            p=[( 0, -0.0728115, -0.263333), ( 0, 0.0676745, -0.30954),
               ( 0, 0.166422, -0.162811), ( 0, 0.316242, 0.066353),
               ( 0, 0.263828, 0.160055), ( 0, 0.0048945, 0.30954),
               ( 0, -0.117923, 0.298165), ( 0, -0.316242, 0.027507),
               ( 0, -0.265623, -0.052244), ( 0, -0.0394945, -0.211749),
               ( 0, 0.190873, 0.097192), ( 0, -0.139762, 0.142256),
               ( 0, -0.0829025, 0.013979), ( 0, -0.0666985, -0.054076),
               ( 0, -0.0205975, 0.039797)],
            k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12]
        )
        cls.rename(node, name)
        return node

    @classmethod
    def transform(cls, name=''):
        node = pm.createNode("transform")
        cls.rename(node, name)
        return node

    @classmethod
    def group(cls, name=''):
        node = pm.group(em=1)
        cls.rename(node, name)
        return node

    @classmethod
    def cube(cls, name=''):
        node = pm.curve(
            d=1,
            p=[(0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5),
               (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5),
               (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5),
               (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5),
               (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),
               (-0.5, 0.5, 0.5)],
            k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        )
        cls.rename(node, name)
        return node

    @classmethod
    def cluster(cls, name=''):
        node = pm.cluster()
        cls.rename(node, name)
        return node[1]
