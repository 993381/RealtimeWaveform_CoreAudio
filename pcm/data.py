import soundfile as sf
import numpy as np
import math


pcm_data = [
            314, 243, 327, 249, 329, 266, 352, 263, 317, 221, 333, 239, 355, 248, 364, 305, 400, 328, 393, 218, 215, 54, 40, -19, -34, -80, -115, -153, -154, -66, -69, -5, -125, 15, -123, -43, -201, -127, -242, -150, -253, -132, -181, -60, -181, -104, -168, -56, -58, -2, 29, 86, 157, 134, 173, 63, 113, 35, 38, 2, -30, -87, -163, -267, -277, -314, -290, -324, -343, -313, -318, -238, -236, -115, -64, 67, 81, 210, 157, 246, 145, 213, 161, 166, 62, 54, -38, 63, 43, 112, 63, 77, 26, -1, -102, -196, -279, -324, -323, -290, -181, -121, 61, 59, 279, 278, 469, 470, 627, 587, 722, 585, 698, 491, 641, 472, 593, 476, 586, 416, 478, 334, 349, 256, 286, 266, 294, 290, 287, 371, 459, 621, 638, 726, 697, 837, 804, 940, 860, 1056, 954, 1140, 1003, 1138, 1019, 1127, 1041, 1145, 1124, 1276, 1246, 1311, 1285, 1337, 1417, 1458, 1576, 1532, 1593, 1478, 1478, 1303, 1339, 1126, 1264, 1103, 1296, 1179, 1390, 1311, 1518, 1484, 1681, 1584, 1708, 1597, 1690, 1672, 1803, 1799, 1873, 1840, 1927, 1920, 2009, 2043, 2117, 2196, 2143, 2229, 2157, 2183, 2126, 2100, 1973, 1976, 1904, 1972, 1940, 2025, 2004, 2127, 2093, 2223, 2178, 2315, 2286, 2406, 2380, 2480, 2461, 2501, 2523, 2499, 2523, 2493, 2492, 2423, 2413, 2280, 2339, 2241, 2283, 2210, 2285, 2262, 2380, 2271, 2380, 2222, 2410, 2255, 2480, 2391, 2552, 2406, 2552, 2425, 2585, 2535, 2668, 2594, 2635, 2569, 2567, 2449, 2376, 2257, 2226, 2208, 2179, 2216, 2201, 2246, 2209, 2291, 2353, 2454, 2493, 2503, 2426, 2398, 2303, 2198, 2033, 1941, 1865, 1790, 1767, 1793, 1814, 1887, 1884, 1920, 1894, 1922, 1887, 1961, 1884, 2000, 1933, 2011, 1912, 1899, 1869, 1837, 1891, 1834, 1810, 1727, 1684, 1677, 1698, 1709, 1747, 1792, 1926, 1946, 2095, 2016, 2067, 1912, 1898, 1758, 1709, 1551, 1473, 1387, 1434, 1390, 1498, 1384, 1494, 1419, 1484, 1466, 1564, 1627, 1745, 1790, 1915, 1919, 1985, 1929, 1897, 1870, 1772, 1719, 1566, 1545, 1425, 1548, 1420, 1680, 1587, 1811, 1720, 1906, 1810, 2005, 1886, 2052, 1863, 2001, 1830, 1909, 1796, 1809, 1709, 1658, 1545, 1479, 1494, 1394, 1483, 1402, 1650, 1642, 1906, 1862, 2039, 2005, 2108, 1991, 2056, 1914, 1997, 1881, 1970, 1978, 2043, 2077, 2089, 2101, 2127, 2152, 2164, 2186, 2178, 2220, 2163, 2177, 2037, 2048, 1919, 1951, 1838, 1927, 1821, 1878, 1795, 1910, 1915, 2110, 2129, 2287, 2256, 2447, 2371, 2459, 2361, 2376, 2301, 2283, 2221, 2182, 2058, 1997, 1859, 1831, 1795, 1840, 1831, 1933, 1970, 2086, 2137, 2167, 2165, 2119, 2140, 2089, 2103, 2043, 2012, 1903, 1959, 1902, 2022, 1921, 1960, 1819, 1821, 1690, 1672, 1573, 1623, 1544, 1670, 1653, 1735, 1710, 1686, 1627, 1600, 1608, 1578, 1503, 1394, 1346, 1231, 1263, 1194, 1235, 1192, 1145, 1069, 985, 895, 861, 753, 774, 748, 794, 812, 784, 841, 881, 1001, 1083, 1237, 1312, 1417, 1439, 1504, 1526, 1551, 1543, 1459, 1321, 1186, 1071, 988, 874, 795, 752, 633, 630, 526, 515, 424, 408, 358, 309, 260, 219, 135, 80, 69, 47, 195, 160, 332, 383, 506, 622, 657, 688, 695, 721, 648, 657
            ]


pcm_data_5120 = [
-117, -82, -335, -401, -603, -690, -958, -989, -1162, -1159, -1117, -987, -877, -686, -539, -411, -231, -47, 21, 54, 48, 36, -82, -243, -451, -624, -938, -1190, -1538, -1735, -1950, -1983, -1916, -1834, -1628, -1402, -1159, -958, -730, -532, -522, -456, -456, -416, -452, -469, -603, -590, -625, -545, -680, -528, -622, -584, -645, -647, -667, -621, -601, -595, -612, -471, -515, -344, -350, -190, -266, -270, -348, -403, -530, -535, -672, -756, -815, -920, -972, -1019, -1042, -1159, -1230, -1255, -1240, -1355, -1410, -1480, -1514, -1595, -1658, -1645, -1532, -1516, -1353, -1261, -1070, -941, -758, -603, -463, -382, -380, -372, -364, -364, -406, -482, -567, -640, -807, -906, -1097, -1070, -1223, -1147, -1185, -1059, -1093, -1034, -1060, -974, -1005, -994, -1140, -1120, -1290, -1345, -1546, -1607, -1708, -1761, -1781, -1860, -1695, -1655, -1505, -1291, -1059, -831, -763, -534, -422, -209, -208, -223, -210, -205, -227, -380, -416, -496, -500, -600, -586, -610, -520, -569, -487, -483, -405, -527, -549, -635, -638, -697, -645, -631, -469, -427, -406, -267, -81, 45, 183, 229, 312, 263, 294, 257, 168, 79, -136, -336, -449, -646, -820, -1046, -1148, -1249, -1352, -1398, -1439, -1393, -1282, -1108, -892, -654, -470, -297, -210, -256, -251, -383, -407, -570, -677, -824, -885, -1014, -1034, -1029, -1002, -1017, -904, -815, -556, -500, -353, -291, -125, -222, -119, -226, -122, -197, -155, -256, -287, -379, -386, -412, -346, -401, -279, -211, -60, -9, 97, 114, 125, 104, 149, 151, 235, 173, 233, 171, 260, 167, 307, 327, 506, 581, 653, 740, 724, 713, 645, 609, 487, 356, 98, -146, -419, -711, -978, -1139, -1203, -1179, -1163, -1065, -1008, -883, -779, -603, -499, -458, -433, -573, -537, -685, -691, -827, -886, -1020, -1075, -1153, -1273, -1269, -1359, -1392, -1440, -1427, -1459, -1361, -1311, -1175, -1120, -964, -953, -917, -927, -858, -915, -903, -915, -937, -821, -783, -666, -713, -545, -492, -273, -207, -155, -185, -216, -353, -521, -667, -842, -1012, -1186, -1314, -1465, -1557, -1719, -1746, -1804, -1803, -1734, -1651, -1510, -1353, -1234, -1035, -1006, -927, -990, -1047, -1246, -1470, -1767, -1911, -2185, -2297, -2564, -2678, -2787, -2808, -2796, -2793, -2801, -2776, -2759, -2730, -2712, -2701, -2653, -2654, -2686, -2676, -2648, -2636, -2611, -2527, -2558, -2518, -2517, -2527, -2437, -2368, -2261, -2134, -2093, -1862, -1832, -1512, -1578, -1448, -1566, -1620, -1677, -1726, -1792, -1788, -1833, -1697, -1727, -1535, -1574, -1375, -1367, -1198, -1182, -1121, -1155, -1318, -1432, -1677, -1778, -1933, -2049, -2216, -2238, -2420, -2401, -2391, -2268, -2173, -2028, -1895, -1744, -1544, -1399, -1295, -1234, -1180, -1165, -1190, -1253, -1315, -1464, -1575, -1803, -1939, -2197, -2243, -2328, -2269, -2318, -2234, -2141, -2081, -1961, -1910, -1814, -1717, -1687, -1578, -1684, -1677, -1916, -1977, -2170, -2213, -2334, -2266, -2208, -2064, -1963, -1820, -1826, -1585, -1488, -1248, -1076, -926, -759, -721, -684, -792, -819, -962, -943, -997, -997, -980, -915, -858, -867, -823, -854, -851, -926, -890, -932, -920, -969, -888, -952, -909, -987, -925, -1033, -972, -1066, -1124, -1175, -1319, -1313, -1328, -1257, -1246, -1279, -1348, -1493, -1605, -1857, -2133, -2372, -2521, -2712, -2739, -2727, -2631, -2493, -2411, -2221, -2153, -1872, -1749, 122, 63, -73, -164, -308, -416, -565, -709, -836, -988, -1030, -1086, -997, -999, -844, -795, -607, -545, -329, -245, -146, -98, -75, -100, -226, -253, -359, -348, -299, -206, -41, 136, 374, 467, 653, 782, 844, 850, 942, 861, 957, 894, 944, 916, 920, 965, 928, 933, 893, 897, 829, 879, 820, 941, 880, 1040, 918, 943, 842, 708, 608, 523, 477, 425, 396, 374, 314, 368, 420, 527, 651, 826, 1042, 1150, 1312, 1413, 1445, 1564, 1503, 1497, 1312, 1208, 1002, 847, 717, 603, 577, 538, 655, 695, 875, 984, 1210, 1341, 1552, 1737, 1781, 1881, 1785, 1814, 1749, 1711, 1687, 1648, 1576, 1627, 1569, 1686, 1754, 1878, 1964, 2090, 2120, 2148, 2143, 2178, 2163, 2193, 2145, 2186, 2179, 2256, 2155, 2185, 2001, 2048, 1916, 2051, 1977, 2104, 2165, 2203, 2223, 2179, 2120, 2017, 1934, 1782, 1641, 1420, 1276, 1113, 960, 877, 891, 785, 854, 859, 1003, 1085, 1259, 1379, 1522, 1586, 1701, 1679, 1645, 1594, 1506, 1285, 1131, 878, 767, 560, 438, 218, 164, -25, 46, -31, 106, 249, 366, 497, 604, 854, 893, 1061, 1115, 1247, 1335, 1499, 1567, 1715, 1775, 1871, 1851, 1801, 1696, 1585, 1617, 1494, 1462, 1400, 1326, 1193, 937, 805, 629, 510, 403, 230, 209, 178, 363, 449, 739, 867, 1215, 1323, 1578, 1619, 1735, 1639, 1616, 1389, 1239, 966, 697, 395, 22, -230, -527, -650, -754, -811, -888, -810, -805, -643, -455, -183, -95, 124, 236, 369, 423, 453, 357, 201, 306, 120, -123, -280, -342, -528, -759, -811, -836, -607, -489, -345, -24, 168, 468, 636, 797, 914, 1084, 1135, 1331, 1284, 1431, 1315, 1392, 1223, 1263, 1348, 1302, 1266, 1309, 1253, 1230, 1237, 1039, 877, 597, 462, 265, 287, 139, 20, -61, 78, 18, 41, -1, 5, 89, 151, 155, 20, 109, -157, -40, -227, -84, -311, -89, -165, -96, -209, -175, -267, -169, -192, -38, -86, 100, 211, 311, 342, 288, 372, 288, 207, 102, -105, -327, -509, -724, -714, -815, -811, -764, -611, -382, -149, 91, 387, 648, 883, 1053, 1207, 1334, 1387, 1504, 1464, 1549, 1440, 1409, 1278, 1145, 1096, 976, 898, 818, 760, 722, 664, 836, 941, 1052, 1137, 1335, 1510, 1584, 1683, 1676, 1816, 1770, 1840, 1805, 1828, 1727, 1715, 1637, 1725, 1673, 1681, 1566, 1587, 1623, 1449, 1283, 1002, 799, 494, 371, 103, 0, -151, -138, -127, 47, 138, 418, 661, 965, 1184, 1504, 1685, 1927, 1949, 2133, 2099, 2078, 1957, 1834, 1726, 1451, 1314, 1107, 1091, 910, 926, 668, 715, 676, 838, 951, 1154, 1420, 1589, 1779, 1886, 2004, 2056, 2042, 2105, 1919, 1879, 1648, 1523, 1198, 1094, 779, 622, 430, 345, 262, 211, 164, 224, 184, 124, 16, -50, -113, -209, -162, -140, 36, 106, 296, 406, 571, 705, 894, 921, 969, 889, 886, 676, 502, 141, -46, -425, -568, -814, -851, -955, -923, -911, -850, -690, -512, -250, -16, 349, 609, 938, 1117, 1316, 1363, 1335, 1229, 1048, 740, 436, 105, -161, -411, -592, -707, -752, -755, -803, -707, -693, -471, -399, -282, -170, 0, 148, 301, 547, 556, 664, 701, 842, 857, 960, 850, 818, 646, 601, 396, 424, 219, 143, -1521, -1472, -1352, -1396, -1232, -1312, -1188, -1224, -1249, -1271, -1375, -1363, -1521, -1468, -1594, -1553, -1649, -1489, -1629, -1437, -1474, -1310, -1265, -1066, -920, -777, -646, -494, -376, -307, -293, -329, -356, -513, -471, -654, -649, -820, -718, -858, -811, -885, -912, -923, -1040, -1017, -1082, -1156, -1261, -1386, -1445, -1492, -1432, -1408, -1320, -1249, -1113, -1085, -1045, -953, -996, -973, -1189, -1217, -1530, -1546, -1792, -1726, -1885, -1757, -1818, -1793, -1742, -1622, -1571, -1403, -1336, -1170, -1021, -700, -443, -172, 35, 80, 208, 179, 173, 69, -76, -180, -346, -470, -674, -683, -816, -847, -1054, -1056, -1190, -1181, -1248, -1193, -1135, -1064, -905, -787, -709, -579, -626, -568, -529, -421, -289, -201, -24, 41, 188, 283, 352, 350, 257, 176, -84, -268, -534, -626, -822, -817, -932, -872, -822, -706, -558, -375, -221, -115, -75, 11, 7, 140, 158, 189, 289, 239, 237, 14, -170, -506, -698, -945, -1094, -1257, -1340, -1376, -1360, -1307, -1199, -1043, -908, -787, -690, -663, -631, -668, -512, -499, -266, -179, 40, 125, 206, 277, 297, 355, 422, 397, 405, 394, 385, 295, 237, 191, 174, 183, 261, 308, 448, 507, 557, 531, 521, 510, 405, 324, 231, 127, -55, -172, -287, -291, -226, -146, -181, -129, -106, -4, -44, 40, 65, 57, 45, 8, 93, 145, 411, 404, 646, 684, 940, 960, 1180, 1253, 1299, 1302, 1236, 1124, 969, 690, 611, 318, 131, -117, -403, -531, -704, -613, -506, -285, -65, 68, 198, 266, 271, 279, 231, 247, 158, 173, 67, 62, 25, 49, 31, 7, -171, -192, -338, -188, -115, 155, 362, 642, 725, 889, 929, 1024, 1027, 1030, 844, 607, 263, -70, -188, -258, -149, 65, 362, 618, 924, 1119, 1306, 1344, 1211, 965, 728, 453, 344, 249, 317, 363, 384, 493, 380, 339, 138, 130, 90, 283, 561, 1091, 1523, 2001, 2239, 2451, 2331, 2065, 1615, 992, 504, 27, -222, -375, -392, -397, -467, -471, -670, -721, -813, -608, -334, 246, 962, 1769, 2573, 3178, 3524, 3495, 3263, 2793, 2272, 1707, 1291, 992, 856, 766, 704, 534, 189, -313, -773, -1154, -1419, -1348, -1064, -548, 158, 864, 1553, 2171, 2624, 3030, 3303, 3655, 3973, 4348, 4599, 4805, 4818, 4553, 3963, 3306, 2429, 1519, 592, -128, -561, -599, -399, 41, 542, 1071, 1467, 1792, 2087, 2475, 2880, 3420, 3991, 4770, 5435, 5967, 6130, 6144, 5652, 4868, 3817, 2868, 1875, 1294, 814, 670, 578, 573, 466, 441, 422, 585, 888, 1428, 2124, 2955, 3829, 4647, 5279, 5817, 6042, 5980, 5696, 5241, 4774, 4257, 3958, 3617, 3381, 3013, 2640, 1982, 1501, 960, 700, 634, 806, 1257, 1739, 2406, 3060, 3735, 4279, 4832, 5159, 5459, 5645, 5838, 6071, 6304, 6545, 6644, 6583, 6251, 5619, 4935, 4149, 3453, 2822, 2414, 2135, 2066, 2182, 2336, 2523, 2597, 2693, 2804, 2961, 3282, 3710, 4390, 4996, 5495, 5737, 5579, 5152, 4611, 3984, 3480, 3012, 2712, 2279, 1848, 1445, 1049, 826, 664, 571, 513, 302, 123, 34, 341, 1061, 2123, 3367, 4344, 4986, 5175, 4837, 4294, 3666, 3203, 2874, 2547, 2256, 1846, 1418, 1089, 788, 610, 460, 361, 310, 326, 692, 1277, 2214, 3213, 4197, 4976, 5395, 5358, 5108, 4767, 4476, 4259, 4117, 3901, 3569, 3069, 2547, 2130, 1847, 1614, 1308, 1013, 564, 196, 23, 253, 833, 1628, 2411, 2970, 3203, 3121, 3003, 3027, 3421, 4032, 4905, 5584, 5863, 5556, 4771, 3723, 2651, 1679, 848, 9, -865, -1727, -2486, -2978, -3079, -2855, -2267, -1610, -900, -255, 485, 1344, 2442, 3754, 5172, 6503, 7498, 7919, 7840, 7338, 6599, 5761, 4801, 3900, 2691, 1624, 462, -462, -1186, -1682, -2064, -2475, -2807, -3077, -3097, -2866, -2306, -1604, -896, -372, -12, 238, 312, 485, 772, 1276, 1758, 2217, 2538, 2658, 2681, 2653, 2728, 2858, 3008, 2908, 2573, 2006, 1500, 1049, 861, 878, 1203, 1491, 1694, 1854, 1879, 2029, 2203, 2575, 2991, 3402, 3533, 3380, 2743, 2043, 1086, 278, -654, -1469, -2569, -3734, -4952, -5968, -6668, -6772, -6552, -5986, -5242, -4418, -3561, -2627, -1542, -471, 731, 1764, 2524, 2916, 2834, 2620, 2235, 1914, 1594, 1249, 823, 284, -356, -815, -1091, -1057, -921, -759, -708, -692, -802, -693, -415, 41, 487, 794, 902, 654, 395, 149, 187, 485, 937, 1372, 1607, 1548, 1270, 849, 564, 403, 313, 167, -186, -684, -1366, -1758, -2049, -1906, -1726, -1404, -1261, -1147, -1157, -942, -519, 174, 1122, 2023, 2624, 2756, 2498, 1784, 1104, 316, -322, -846, -1360, -1987, -2591, -3118, -3330, -3317, -2997, -2506, -1982, -1359, -788, -20, 748, 1666, 2465, 3099, 3479, 3429, 3053, 2482, 1853, 1390, 1011, 783, 557, 166, -203, -641, -838, -917, -868, -793, -858, -1018, -1235, -1224, -950, -514, 16, 315, 367, 69, -243, -558, -472, -98, 491, 1136, 1550, 1677, 1408, 1127, 782, 566, 409, 236, -189, -681, -1297, -1771, -1957, -1746, -1350, -850, -533, -360, -188, 35, 554, 1149, 1832, 2341, 2497, 2208, 1509, 610, -286, -1171, -1820, -2378, -2706, -3061, -3222, -3389, -3183, -2928, -2361, -1850, -1263, -720, -151, 556, 1373, 2160, 2857, 3201, 3220, 2833, 2271, 1602, 1019, 570, 144, -159, -435, -698, -993, -1145, -1274, -1285, -1226, -1229, -1290, -1384, -1445, -1258, -878, -335, 209, 583, 735, 551, 369, 194, 250, 550, 944, 1376, 1574, 1442, 1128, 505, -28, -600, -938, -1301, -1597, -1952, -2219, -2332, -2265, -1881, -1352, -730, -186, 224, 525, 873, 1256, 1851, 2386, 2840, 2934, 2597, 1986, 1000, 17, -949, -1708, -2328, -2764, -3125, -3282, -3277, -3035, -2584, -1950, -1288, -622, 26, 601, 1346, 1939, 2618, 3038, 3263, 3074, 2712, 2069, 1465, 780, 352, -100, -410, -826, -1194, -1407, -1520, -1476, -1306, -1086, -843, -728, -695, -607, -463, -99, 168, 503, 646, 711, 660, 584, 601, 785, 1093, 1479, 1693, 1690, 1388, 830, 231, -419, -862, -1157, -1360, -1409, -1597, -1671, -1827, -1703, -1490, -945, -326, 377, 869, 1437, 1786, 2235, 2587, 2833, 2903, 2616, 1925, 930, -222, -1384, -2274, -2884, -3222, -3432, -3535, -3504, -3376, -3090, -2650, -2029, -1254, -467, 299, 931, 1543, 2072, 2578, 2799, 2791, 2382, 1708, 940, 181, -405, -784, -950, -1088, -1281, -1602, -2043, -2392, -2592, -2692, -2606, -2525, -2341, -2127, -1859, -1525, -969, -399, 238, 564, 771, 642, 497, 419, 562, 862, 1294, 1488, 1474, 1028, 372, -512, -1311, -1895, -2236, -2452, -2610, -2671, -2731, -2700, -2564, -2253, -1764, -1231, -702, -239, 200, 534, 764, 994, 1137, 1046, 712, -71, -965, -2046, -2977, -3703, -4089, -4198, -4124, -4027, -3849, -3614, -3337, -2970, -2507, -1980, -1544, -1062, -737, -365, -72, 230, 299, 165, -232, -934, -1692, -2445, -3053, -3288, -3427, -3377, -3317, -3365, -3498, -3624, -3639, -3512, -3355, -3104, -2994, -2865, -2749, -2659, -2328, -1971, -1409, -1040, -619, -447, -332, -238, -96, 169, 404, 516, 389, -35, -678, -1460, -2213, -2770, -3169, -3358, -3457, -3546, -3598, -3617, -3512, -3158, -2709, -2130, -1609, -1148, -847, -597, -453, -386, -501, -744, -1322, -2055, -2964, -3908, -4658, -5357, -5656, -5761, -5564, -5349, -4939, -4520, -3925, -3376, -2664, -2192, -1633, -1327, -949, -740, -518, -464, -479, -800, -1170, -1730, -2246, -2727, -2944, -2928, -2760, -2637, -2616, -2801, -2967, -3186, -3300, -3419, -3341, -3236, -3158, -3064, -2985, -2777, -2455, -2021, -1508, -1016, -579, -283, -12, 186, 512, 705, 951, 966, 730, 207, -520, -1422, -2202, -2798, -3247, -3511, -3668, -3806, -3803, -3781, -3457, -2972, -2273, -1521, -839, -241, 227, 548, 725, 714, 504, -34, -666, -1465, -2282, -2993, -3598, -3992, -4200, -4302, -4425, -4350, -4278, -3959, -3709, -3183, -2866, -2455, -2142, -1779, -1435, -1044, -735, -394, -317, -387, -684, -1087, -1490, -1854, -2026, -2095, -2107, -2073, -2166, -2374, -2768, -3005, -3356, -3483, -3550, -3502, -3449, -3358, -3157, -2910, -2625, -2154, -1672, -1023, -547, -186, 27, 171, 172, 282, 228, 211, -95, -562, -1258, -2076, -2913, -3641, -4156, -4430, -4623, -4548, -4486, -4172, -3771, -3265, -2726, -2084, -1518, -1054, -722, -502, -391, -416, -615, -1076, -1607, -2450, -3219, -3909, -4414, -4662, -4768, -4774, -4654, -4527, -4273, -4131, -3733, -3401, -2982, -2717, -2456, -2323, -2176, -2016, -1771, -1492, -1332, -1259, -1294, -1486, -1680, -1899, -1919, -1783, -1542, -1266, -1122, -1227, -1422, -1789, -2059, -2279, -2304, -2165, -1916, -1690, -1386, -1150, -863, -593, -239, 20, 317, 504, 571, 426, 293, -59, -316, -823, -1338, -2005, -2667, -3469, -4043, -4512, -4639, -4575, -4174, -3718, -3158, -2575, -1975, -1344, -730, -96, 410, 894, 1150, 1358, 1309, 1187, 921, 454, -137, -714, -1374, -1837, -2252, -2347, -2285, -2059, -1793, -1617, -1434, -1253, -1098, -843, -550, -219, 31, 107, 173, 178, 221, 257, 264, 198, 54, -107, -282, -375, -364, -214, -77, 187, 171, 115, -154, -388, -597, -531, -392, -71, 244, 619, 935, 1180, 1379, 1612, 1868, 2041, 2329, 2443, 2595, 2527, 2384, 2082, 1774, 1297, 756, 123, -482, -1141, -1601, -2036, -2166, -2150, -1931, -1627, -1198, -734, -203, 322, 900, 1490, 2038, 2408, 2638, 2684, 2616, 2215, 1818, 1217, 727, 147, -190, -522, -564, -595, -388, -174, 131, 280, 534, 628, 860, 1003, 1342, 1548, 1797, 1902, 1899, 1930, 1761, 1728, 1535, 1430, 1240, 1144, 1044, 1043, 1121, 1283, 1456, 1514, 1482, 1285, 1069, 853, 720, 733, 998, 1286, 1739, 2051, 2473, 2646, 2889, 3027, 3272, 3405, 3533, 3602, 3580, 3471, 3205, 2821, 2319, 1728, 965, 274, -433, -951, -1252, -1352, -1168, -817, -301, 300, 897, 1440, 1917, 2293, 2628, 2997, 3260, 3506, 3767, 3820, 3747, 3498, 2992, 2481, 1845, 1325, 853, 558, 458, 460, 663, 809, 1036, 1089, 1248, 1184, 1275, 1277, 1444, 1591, 1800, 1905, 2063, 2046, 2008, 1843, 1650, 1445, 1237, 1000, 935, 928, 992, 1041, 1096, 1148, 1125, 921, 724, 372, 220, 100, 256, 501, 872, 1276, 1651, 2057, 2322, 2552, 2768, 2901, 2973, 2958, 2788, 2588, 2167, 1803, 1341, 734, 174, -459, -998, -1428, -1711, -1671, -1402, -907, -265, 438, 1178, 1862, 2448, 2963, 3388, 3620, 3852, 3855, 3841, 3576, 3183, 2590, 1978, 1207, 534, -165, -576, -918, -984, -930, -727, -548, -352, -270, -140, -59, 96, 342, 675, 1121, 1513, 1825, 2110, 2294, 2418, 2531, 2575, 2571, 2526, 2401, 2249, 2169, 2037, 1995, 1801, 1608, 1287, 840, 410, -60, -267, -383, -203, 138, 623, 1210, 1759, 2358, 2809, 3208, 3495, 3722, 3783, 3797, 3581, 3222, 2735, 2186, 1502, 839, 127, -395, -923, -1133, -1225, -1057, -659, -137, 416, 1064, 1559, 2154, 2573, 3017, 3258, 3510, 3547, 3584, 3405, 3116, 2771, 2342, 1917, 1410, 939, 462, 78, -167, -245, -355, -381, -448, -554, -621, -766, -674, -625, -281, 46, 553, 864, 1201, 1370, 1494, 1546, 1539, 1496, 1412, 1366, 1189, 1071, 901, 699, 454, 280, 81, -181, -328, -511, -506, -551, -239, 49, 664, 1198, 1792, 2292, 2645, 2918, 3017, 3109, 3102, 2991, 2870, 2615, 2270, 1877, 1287, 813, 250, -226, -670, -902, -1016, -974, -751, -403, 25, 569, 1026, 1494, 1925, 2242, 2555, 2573, 2737, 2530, 2502, 2203, 1965, 1636, 1116, 755, 152, -284, -747, -1112, -1326, -1432, -1418, -1353, -1333, -1232, -1138, -985, -910, -618, -424, -145, 114, 388, 584, 750, 883, 874, 897, 864, 723, 707, 499, 456, 231, 34, -172, -404, -639, -937, -1057, -1183, -1140, -1047, -732, -337, 138, 661, 1243, 1716, 2148, 2368, 2541, 2479, 2415, 2100, 1838, 1460, 1096, 613, 95, -353, -888, -1187, -1453, -1512, -1543, -1451, -1193, -921, -551, -173, 252, 594, 1012, 1315, 1481, 1638, 1639, 1648, 1486, 1272, 1176, 809, 594, 92, -234, -672, -1025, -1167, -1319, -1419, -1497, -1476, -1538, -1318, -1232, -994, -676, -273, 12, 438, 864, 1326, 1686, 1939, 2132, 2239, 2245, 2101, 1869, 1657, 1232, 969, 687, 209, -78, -359, -673, -824, -951, -822, -794, -431, -65, 463, 1039, 1661, 2178, 2743, 3052, 3243, 3302, 3126, 2941, 2642, 2209, 1720, 1239, 737, 175, -283, -844, -1133, -1589, -1652, -1781, -1570, -1415, -1094, -678, -271, 169, 508, 824, 1264, 1297, 1611, 1643, 1657, 1441, 1388, 1077, 758, 430, -158, -440, -845, -1153, -1553, -1834, -1651, -1721, -1573, -1457, -1361, -832, -801, -549, -39, 198, 772, 1176, 1447, 1873, 2011, 2332, 2226, 2289, 2218, 1996, 1774, 1726, 1141, 1014, 714, 103, -138, -531, -961, -1015, -974, -953, -449, -246, 466, 929, 1718, 2145, 2393, 2831, 2769, 2631, 2788, 2085, 2034, 1612, 1256, 870, 325, -161, -431, -769, -1069, -1428, -1384, -1237, -1149, -629, -560, 2, 366, 730, 898, 1259, 1032, 1428, 1316, 1261, 983, 815, 519, 343, -103, -168, -719, -865, -1145, -1559, -1579, -1798, -1648, -1635, -1716, -1596, -1510, -1469, -928, -838, -226, 115, 732, 1113, 1545, 1843, 2203, 2023, 2085, 1663, 1423, 1018, 628, 236, -186, -520, -958, -1207, -1501, -1384, -1743, -1474, -1590, -1120, -718, -197, 293, 1071, 1334, 1796, 1894, 2029, 1897, 1842, 1691, 1454, 1340, 805, 450, -25, -48, -760, -1140, -1752, -1864, -1990, -1845, -1670, -1229, -1046, -610, -459, -40, 160, 245, 534, 432, 683, 387, 530, 401, 280, 120, 14, -305, -427, -808, -853, -1125, -1135, -1292, -1255, -1222, -1010, -949, -764, -484, -324, -176, -28, 290, 609, 928, 1389, 1754, 1980, 2166, 2049, 2163, 1938, 1897, 1683, 1435, 1095, 690, 351, -21, -256, -617, -857, -1010, -1028, -851, -555, -166, 356, 913, 1437, 1889, 2367, 2580, 2831, 2855, 2755, 2548, 2354, 1996, 1716, 1236, 881, 427, 171, -225, -535, -665, -739, -513, -360, -191, 68, 345, 683, 866, 1093, 1252, 1482, 1709, 1995, 2206, 2369, 2472, 2463, 2451, 2242, 2075, 1798, 1603, 1217, 891, 392, 125, -182, -382, -452, -429, -377, -223, -45, 287, 654, 1036, 1618, 2039, 2616, 2847, 3108, 3193, 2983, 2750, 2459, 2002, 1674, 1077, 589, 141, -301, -483, -819, -885, -1014, -824, -555, -83, 244, 971, 1250, 1911, 2194, 2550, 2681, 2890, 2971, 2923, 2745, 2653, 2425, 2275, 1933, 1520, 1252, 689, 348, -184, -461, -856, -848, -950, -840, -796, -590, -443, -227, -9, 140, 221, 341, 406, 687, 810, 1012, 1074, 919, 875, 723, 448, 227, -204, -281, -742, -948, -1291, -1450, -1654, -1671, -1831, -1726, -1744, -1475, -1189, -950, -435, -172, 287, 319, 554, 435, 488, 205, 43, -369, -509, -993, -1143, -1701, -1908, -2323, -2543, -2807, -2782, -2789, -2730, -2481, -2086, -1702, -1260, -807, -289, 98, 423, 489, 643, 625, 493, 535, 303, 253, -94, -233, -720, -979, -1530, -1882, -2160, -2337, -2549, -2588, -2604, -2386, -2268, -1962, -1805, -1406, -1225, -994, -654, -509, -267, -172, 138, 182, 275, 129, -60, -337, -653, -1203, -1580, -2099, -2368, -2740, -2931, -3128, -3134, -3046, -3040, -2705, -2459, -2001, -1610, -1108, -623, -143, 191, 398, 447, 511, 197, -57, -567, -879, -1411, -1741, -2394, -2760, -3152, -3453, -3625, -3555, -3486, -3246, -2928, -2448, -1897, -1329, -804, -311, 295, 658, 941, 1066, 1100, 1166, 950, 854, 556, 367, 103, -188, -678, -1046, -1607, -2008, -2270, -2404, -2648, -2670, -2473, -2328, -2136, -2020, -1889, -1609, -1280, -1112, -806, -678, -562, -428, -230, -183, -251, -536, -921, -1384, -1944, -2453, -2905, -3237, -3631, -3726, -3921, -3862, -3914, -3543, -3326, -2820, -2594, -2129, -1705, -1094, -755, -264, 18, 235, 77, -19, -311, -648, -1072, -1415, -1758, -2128, -2468, -2636, -2780, -2896, -2909, -2818, -2584, -2410, -2147, -1849, -1426, -1092, -762, -394, -29, 221, 252, 266, 219, 4, -153, -380, -459, -652, -900, -1134, -1470, -1920, -2306, -2614, -2669, -2594, -2673, -2427, -2289, -1957, -1772, -1567, -1367, -1258, -1057, -811, -594, -277, -72, 306, 456, 627, 471, 313, -92, -585, -1052, -1748, -2017, -2531, -2646, -3039, -3074, -3177, -3076, -3064, -2741, -2632, -2123, -1929, -1315, -1020, -341, -28, 446, 540, 583, 311, 53, -280, -752, -1090, -1437, -1496, -1626, -1576, -1661, -1506, -1473, -1294, -1197, -903, -682, -381, -69, 383, 720, 1132, 1134, 1350, 1197, 1101, 922, 637, 460, 169, -123, -415, -644, -978, -1313, -1832, -2176, -2760, -2899, -3172, -3164, -3087, -2880, -2627, -2359, -2046, -1814, -1596, -1439, -1152, -1009, -693, -589, -323, -342, -387, -690, -1009, -1533, -1950, -2527, -2837, -3189, -3190, -3247, -3074, -2962, -2610, -2449, -2126, -1848, -1514, -1138, -870, -452, -208, -22, 242, 246, 382, 153, -35, -342, -791, -1005, -1483, -1664, -1848, -1911, -2089, -2137, -2180, -2037, -2028, -1784, -1576, -1175, -687, -295, 183, 665, 906, 1193, 1276, 1252, 1122, 993, 837, 665, 557, 146, -215, -680, -995, -1464, -1838, -2244, -2485, -2553, -2569, -2364, -2095, -1771, -1503, -1067, -683, -435, -88, 192, 485, 690, 830, 978, 1045, 998, 825, 601, 322, -109, -358, -719, -946, -1260, -1509, -1609, -1738, -1593, -1621, -1334, -1095, -722, -311, 98, 681, 1207, 1681, 1980, 2156, 2189, 2062, 1900, 1599, 1193, 897, 420, 202, -35, -159, -246, -230, -171, -207, -114, -109, 93, 271, 627, 975, 1412, 1624, 1893, 2031, 2154, 2205, 2277, 2276, 2283, 2178, 2020, 1899, 1786, 1593, 1279, 1121, 648, 303, -74, -256, -464, -436, -455, -306, -197, 42, 171, 523, 744, 1147, 1383, 1756, 1935, 2212, 2339, 2381, 2473, 2281, 2116, 1638, 1318, 806, 358, 18, -129, -286, -152, -174, 41, 158, 495, 742, 1165, 1448, 1852, 2058, 2319, 2471, 2533, 2546, 2415, 2290, 2173, 1881, 1685, 1452, 1169, 1101, 880, 893, 780, 930, 899, 1038, 1062, 1310, 1425, 1743, 1854, 2166, 2245, 2521, 2505, 2511, 2307, 2259, 2043, 1908, 1643, 1414, 1242, 1055, 785, 593, 374, 291, 111, -16, -211, -253, -184, -58, 230, 476, 710, 852, 1140, 1279, 1545, 1812, 2151, 2384, 2608, 2660, 2758, 2749, 2693, 2431, 2205, 1877, 1428, 1046, 657, 412, 186, 35, 37, 1, 166, 257, 436, 642, 885, 1104, 1272, 1463, 1638, 1734, 1841, 1889, 1913, 1774, 1504, 1304, 886, 580, 347, 283, 224, 194, 233, 307, 490, 513, 520, 670, 689, 853, 962, 1133, 1250, 1285, 1376, 1294, 1334, 1189, 1217, 1139, 1211, 1122, 1184, 1045, 1003, 687, 519, 85, -105, -514, -647, -937, -970, -1043, -860, -564, -157, 207, 519, 932, 1249, 1564, 1799, 2024, 2148, 2155, 2070, 1968, 1635, 1341, 924, 323, -153, -764, -1187, -1486, -1496, -1455, -1413, -1321, -1040, -1026, -613, -505, -61, 301, 604, 872, 1109, 1213, 1379, 1337, 1269, 1044, 884, 629, 434, 282, 131, -34, -70, -124, -78, -203, -385, -625, -629, -650, -588, -545, -303, -110, 107, 416, 595, 861, 1001, 1080, 1036, 994, 953, 801, 623, 464, 144, -169, -450, -724, -964, -1196, -1556, -1650, -1723, -1709, -1472, -1297, -870, -581, -152, 254, 529, 956, 1153, 1455, 1587, 1426, 1262, 949, 690, 341, -221, -698, -1273, -1602, -2116, -2270, -2246, -2276, -2049, -1936, -1756, -1803, -1500, -1466, -1205, -991, -860, -670, -580, -506, -515, -620, -692, -827, -934, -1077, -1282, -1347, -1471, -1474, -1402, -1287, -1216, -1043, -1022, -875, -809, -693, -482, -313, -87, 76, 226, 294, 337, 441, 399, 442, 491, 534, 484, 455, 398, 151, -86, -418, -696, -1016, -1272, -1567, -1736, -1687, -1664, -1480, -1199, -903, -479, -207, 124, 369, 675, 801, 1052, 890, 895, 597, 408, 58, -381, -800, -1255, -1749, -2085, -2417, -2604, -2586, -2527, -2338, -1990, -1694, -1312, -1130, -741, -510, -220, -44, 173, 298, 409, 363, 330, 217, 60, -37, -286, -326, -498, -555, -645, -660, -681, -688, -656, -602, -565, -509, -494, -390, -179, 33, 312, 636, 902, 1239, 1538, 1793, 1922, 2001, 2094, 2028, 1894, 1690, 1522, 1116, 820, 457, 146, -191, -535, -805, -1000, -1124, -1029, -843, -464, -117, 230, 636, 1009, 1385, 1759, 1952, 2151, 2169, 2112, 1897, 1558, 1208, 733, 333, -220, -518, -962, -1116, -1325, -1270, -1205, -1046, -743, -465, -232, 35, 267, 469, 748, 932, 1147, 1286, 1559, 1623, 1786, 1670, 1606, 1414, 1284, 1138, 1045, 1062, 895, 933, 731, 751, 623, 678, 670, 695, 744, 804, 853, 1042, 1262, 1501, 1639, 1823, 2025, 2193, 2423, 2526, 2571, 2602, 2494, 2302, 2098, 1722, 1380, 1065, 715, 299, -13, -346, -501, -556, -436, -118, 237, 718, 1098, 1501, 1825, 2096, 2353, 2466, 2445, 2283, 2054, 1618, 1285, 718, 308, -241, -530, -1006, -1130, -1316, -1362, -1342, -1049, -805, -357, -30, 309, 681, 1009, 1303, 1592, 1936, 2194, 2444, 2523, 2718, 2828, 3005, 2919, 2925, 2846, 2730, 2568, 2424, 2323, 2172, 1967, 1720, 1564, 1366, 1192, 1092, 1090, 1220, 1334, 1582, 1888, 2211, 2427, 2667, 2802, 3086, 3050, 3128, 3019, 2952, 2765, 2587, 2401, 2098, 1848, 1467, 1210, 955, 792, 720, 724, 774, 1075, 1252, 1631, 1830, 2212, 2399, 2595, 2773, 2818, 2824, 2862, 2775, 2656, 2452, 2164, 1869, 1543, 1176, 828, 522, 262, 82, 6, 80, 296, 561, 831, 1046, 1414, 1565, 1837, 2091, 2348, 2609, 2879, 3047, 3143, 3236, 3184, 3063, 2830, 2644, 2330, 2195, 1967, 1806, 1693, 1650, 1533, 1470, 1277, 1252, 1220, 1180, 1171, 1263, 1459, 1786, 2071, 2434, 2710, 2873, 3105, 3025, 3102, 2946, 2826, 2575, 2379, 2017, 1635, 1278, 923, 519, 288, -109, -296, -582, -565, -626, -474, -309, 66, 370, 656, 840, 974, 1124, 1294, 1359, 1311, 1204, 990, 746, 310, -34, -467, -771, -1198, -1299, -1561, -1522, -1535, -1362, -1188, -984, -719, -502, -262, -46, 48, 219, 321, 382, 489, 482, 472, 372, 174, 10, -70, -245, -360, -558, -659, -863, -1102, -1313, -1596, -1791, -2083, -2268, -2380, -2555, -2543, -2543, -2367, -2225, -1981, -1792, -1592, -1475, -1441, -1398, -1318, -1408, -1301, -1520, -1537, -1885, -2048, -2397, -2558, -2780, -2894, -2996, -3034, -3038, -2938, -2783, -2537, -2186, -1988, -1741, -1639, -1470, -1498, -1416, -1487, -1640, -1844, -2167, -2512, -2803, -3032, -3302, -3450, -3761, -3798, -3773, -3672, -3569, -3164, -2995, -2650, -2416, -2142, -1964, -1622, -1552, -1461, -1335, -1355, -1262, -1259, -1170, -1415, -1484, -1680, -1814, -1992, -2215, -2467, -2434, -2672, -2694, -2836, -2817, -2872, -2795, -2816, -2812, -2741, -2735, -2572, -2318, -2115, -1762, -1497, -1201, -1026, -856, -875, -749, -766, -746, -936, -923, -1271, -1431, -1776, -2056, -2336, -2676, -2795, -2941, -2895, -2934, -2673, -2425, -2084, -1741, -1362, -1232, -929, -875, -807, -817, -917, -1018, -1233, -1374, -1721, -1925, -2364, -2476, -2843, -2940, -3156, -3033, -3003, -2864, -2636, -2455, -2201, -1980, -1887, -1718, -1622, -1465, -1305, -1193, -1052, -1003, -915, -909, -969, -1158, -1311, -1540, -1691, -1870, -1982, -2135, -2328, -2431, -2640, -2825, -2977, -3027, -3084, -3135, -3059, -2887, -2682, -2367, -1996, -1640, -1295, -1017, -905, -837, -844, -831, -865, -971, -1162, -1460, -1762, -2084, -2506, -2776, -3038, -3093, -3071, -3010, -2633, -2251, -1821, -1354, -929, -466, -131, 203, 382, 515, 529, 414, 185, 21, -302, -701, -1084, -1474, -1898, -2248, -2533, -2746, -2774, -2830, -2792, -2679, -2580, -2413, -2166, -1859, -1568, -1334, -1054, -900, -615, -552, -404, -342, -292, -394, -494, -702, -875, -1114, -1281, -1494, -1538, -1690, -1766, -1828, -1761, -1749, -1642, -1510, -1315, -1061, -730, -503, -114, 236, 652, 969, 1296, 1486, 1694, 1758, 1736, 1600, 1427, 1158, 1010, 797, 463, 278, -108, -316, -742, -956, -1256, -1351, -1321, -1235, -1091, -836, -549, -194, 156, 362, 483, 594, 527, 541, 389, 111, -19, -295, -528, -830, -1029, -1219, -1329, -1319, -1383, -1286, -1203, -1040, -860, -623, -546, -417, -327, -206, -155, -137, -114, -21, 104, 168, 178, 193, 94, 89, -24, -139, -219, -361, -321, -461, -591, -796, -1019, -1089, -1146, -1085, -1059, -831, -546, -285, -21, 245, 595, 876, 1101, 1243, 1381, 1406, 1390, 1259, 1130, 810, 493, 161, -156, -499, -918, -1195, -1447, -1568, -1596, -1508, -1210, -927, -496, -188, 231, 505, 686, 747, 704, 630, 526, 334, 103, -138, -465, -730, -985, -1245, -1486, -1800, -1960, -2154, -2143, -2153, -1969, -1803, -1589, -1405, -1095, -841, -516, -295, -117, 38, 138, 328, 487, 574, 689, 690, 654, 503, 389, 215, -14, -130, -318, -480, -564, -721, -817, -826, -669, -635, -406, -228, -11, 174, 556, 869, 1296, 1577, 1779, 1851, 1830, 1745, 1569, 1324, 988, 593, 214, -212, -530, -853, -1139, -1392, -1551, -1669, -1687, -1620, -1461, -1275, -995, -760, -485, -254, -162, -127, -191, -238, -348, -434, -604, -629, -864, -1047, -1314, -1424, -1491, -1495, -1347, -1228, -1106, -933, -677, -439, -116, 32, 266, 410, 564, 590, 699, 795, 942, 998, 1079, 1077, 1084, 1023, 888, 790, 492, 244, -5, -178, -298, -398, -507, -508, -522, -487, -459, -311, -88, 189, 517, 715, 916, 1145, 1426, 1673, 1936, 2016, 2123, 2074, 1928, 1743, 1316, 985, 525, 34, -423, -856, -1208, -1501, -1649, -1757, -1704, -1527, -1194, -791, -452, -126, 136, 350, 471, 491, 449, 412, 243, 235, 36, -32, -240, -422, -488, -645, -751, -875, -955, -966, -953, -787, -674, -437, -267, -80, 23, 194, 258, 418, 462, 701, 741, 874, 976, 1163, 1199, 1103, 999, 880, 673, 482, 289, 125, -93, -195, -363, -418, -461, -349, -197, 28, 329, 672, 1067, 1391, 1755, 1954, 2133, 2317, 2423, 2514, 2382, 2332, 2083, 1931, 1595, 1247, 828, 422, -27, -383, -691, -782, -886, -818, -674, -463, -162, 195, 582, 996, 1246, 1563, 1730, 1927, 1977, 1974, 1990, 1814, 1817, 1561, 1384, 1114, 868, 599, 374, 214, 87, 76, 151, 299, 500, 685, 967, 1180, 1418, 1593, 1744, 1873, 2017, 2123, 2154, 2148, 2250, 2306, 2357, 2371, 2331, 2179, 2039, 1870, 1792, 1631, 1501, 1321, 1240, 1241, 1229, 1281, 1391, 1537, 1776, 1947, 2166, 2400, 2631, 2929, 3103, 3271, 3311, 3233, 3065, 2876, 2548, 2277, 1891, 1516, 1129, 811, 564, 551, 625, 698, 933, 1021, 1240, 1427, 1723, 2057, 2425, 2758, 3044, 3176, 3351, 3432, 3501, 3549, 3619, 3621, 3662, 3631, 3515, 3475, 3273, 3163, 2993, 2892, 2801, 2722, 2661, 2698, 2729, 2766, 2756, 2766, 2803, 2818, 2897, 2993, 3146, 3210, 3293, 3410, 3655, 3676, 3762, 3710, 3686, 3496, 3272, 2954, 2725, 2465, 2352, 2131, 2225, 2199, 2246, 2344, 2451, 2621, 2807, 3030, 3283, 3548, 3793, 4055, 4291, 4471, 4523, 4516, 4435, 4183
]


_audio_path = 'source_normal.wav'

class PCM_data_provider:
    def __init__(self):
        data, samplerate = sf.read(_audio_path, dtype='int16')
        self.data = data
        self.samplerate = samplerate

    def get_data_at(self, time: float, duration: float) -> np.ndarray:
        start = math.floor(time * self.samplerate)
        end = start + math.floor(duration * self.samplerate)
        data = self.data[start:end]
        return data


if __name__ == '__main__':
    d = PCM_data_provider()
    print(d.get_data_at(0, 0.1))