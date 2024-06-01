from typing import List, Tuple


from batteryml.builders import TRAIN_TEST_SPLITTERS
from batteryml.train_test_split.base import BaseTrainTestSplitter


@TRAIN_TEST_SPLITTERS.register()
class MIX100TrainTestSplitter(BaseTrainTestSplitter):
    def __init__(self, cell_data_path: str):
        BaseTrainTestSplitter.__init__(self, cell_data_path)
        test_ids = [
            "HUST_1-1",
            "MATR_b3c42",
            "RWTH_011",
            "RWTH_032",
            "MATR_b2c27",
            "MATR_b1c4",
            "MATR_b4c15",
            "RWTH_040",
            "MATR_b1c16",
            "HUST_1-8",
            "RWTH_015",
            "MATR_b3c34",
            "MATR_b4c38",
            "UL-PUR_N10-NA7_18650_NCA_23C_0-100_0.5-0.5C_g",
            "MATR_b3c25",
            "CALCE_CS2_35",
            "UL-PUR_N20-EX2_18650_NCA_23C_0-100_0.5-0.5C_b",
            "HUST_5-1",
            "MATR_b3c26",
            "MATR_b1c26",
            "HUST_4-4",
            "MATR_b4c4",
            "HUST_8-4",
            "RWTH_030",
            "MATR_b3c14",
            "HNEI_18650_NMC_LCO_25C_0-100_0.5-1.5C_e",
            "RWTH_003",
            "MATR_b2c26",
            "MATR_b1c45",
            "MATR_b1c40",
            "MATR_b4c19",
            "HUST_3-6",
            "MATR_b3c24",
            "MATR_b2c12",
            "MATR_b3c17",
            "HUST_5-2",
            "MATR_b1c32",
            "MATR_b2c30",
            "MATR_b2c11",
            "MATR_b1c15",
            "HUST_7-5",
            "HUST_2-6",
            "MATR_b3c35",
            "RWTH_036",
            "HUST_10-8",
            "MATR_b4c41",
            "UL-PUR_N10-OV8_18650_NCA_23C_0-100_0.5-0.5C_h",
            "MATR_b4c22",
            "MATR_b1c42",
            "MATR_b2c43",
            "MATR_b1c19",
            "HUST_1-4",
            "RWTH_048",
            "HNEI_18650_NMC_LCO_25C_0-100_0.5-1.5C_a",
            "UL-PUR_N15-OV3_18650_NCA_23C_0-100_0.5-0.5C_c",
            "RWTH_045",
            "RWTH_028",
            "MATR_b2c23",
            "HUST_3-4",
            "RWTH_034",
            "MATR_b2c34",
            "MATR_b3c16",
            "MATR_b2c33",
            "MATR_b1c35",
            "MATR_b3c15",
            "MATR_b3c33",
            "HUST_8-7",
            "HUST_10-2",
            "MATR_b4c33",
            "MATR_b1c31",
            "HUST_4-2",
            "HUST_8-6",
            "UL-PUR_N20-NA6_18650_NCA_23C_0-100_0.5-0.5C_f",
            "MATR_b1c7",
            "MATR_b3c11",
            "RWTH_012",
            "MATR_b3c10",
            "MATR_b4c16",
            "MATR_b3c41",
            "RWTH_027",
            "RWTH_005",
            "MATR_b4c43",
            "HUST_6-2",
            "HNEI_18650_NMC_LCO_25C_0-100_0.5-1.5C_l",
            "MATR_b3c12",
            "MATR_b2c1",
            "HUST_4-6",
            "MATR_b3c21",
            "RWTH_039",
            "MATR_b4c26",
            "MATR_b3c2",
            "MATR_b4c8",
            "MATR_b3c22",
            "CALCE_CX2_34",
            "MATR_b1c5",
            "RWTH_019",
            "CALCE_CX2_36",
            "HUST_6-6",
            "RWTH_037",
            "MATR_b4c20",
            "HUST_10-1",
            "MATR_b4c29",
            "HUST_9-4",
            "HUST_8-1",
            "MATR_b4c7",
            "MATR_b3c32",
            "MATR_b4c0",
            "MATR_b2c2",
            "RWTH_041",
            "HUST_10-4",
            "MATR_b2c13",
            "MATR_b4c42",
            "RWTH_044",
            "RWTH_035",
            "MATR_b3c20",
            "HNEI_18650_NMC_LCO_25C_0-100_0.5-1.5C_t",
            "HUST_4-1",
            "HUST_10-7",
            "MATR_b3c40",
            "HUST_8-8",
            "RWTH_023",
            "HUST_7-3",
            "MATR_b1c18",
            "HNEI_18650_NMC_LCO_25C_0-100_0.5-1.5C_s",
            "MATR_b4c1",
            "MATR_b1c8",
            "HUST_9-7",
            "MATR_b2c25",
            "MATR_b2c36",
            "MATR_b3c13",
            "MATR_b2c19",
            "MATR_b2c47",
            "MATR_b4c34",
            "MATR_b4c2",
            "RWTH_002",
            "MATR_b3c19",
            "MATR_b4c9",
        ]

        self.train_cells, self.test_cells = [], []
        for filename in self._file_list:
            # filename like: HUST_1-1.pkl
            if filename.stem in test_ids:
                self.test_cells.append(filename)
            else:
                self.train_cells.append(filename)

    def split(self) -> Tuple[List, List]:
        return self.train_cells, self.test_cells