# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 17:06:59 2024

@author: sanga
"""

import os
cwd = os.chdir('C:\\Users\\sanga\\OneDrive\\Desktop\\Research\\Apostolova_Lab\\IMAGENE\\MRI_QC_scripts')

filename = [
    'E001_V1_2008-10-02_denoised.nii',
    'E001_V2_2009-10-16_denoised.nii',
    'E001_V3_2010-09-29_denoised.nii',
    'E001_V4_2011-11-02_denoised.nii',
    'E001_V5_2013-03-05_denoised.nii',
    'E002_V1_2008-10-03_denoised.nii',
    'E002_V2_2009-09-16_denoised.nii',
    'E003_V1_2008-10-16_denoised.nii',
    'E003_V2_2009-09-16_denoised.nii',
    'E003_V3_2010-10-13_denoised.nii',
    'E004_V1_2008-10-07_denoised.nii',
    'E004_V2_2009-11-24_denoised.nii',
    'E004_V3_2010-12-15_denoised.nii',
    'E004_V4_2012-03-07_denoised.nii',
    'E004_V5_2012-12-14_denoised.nii',
    'E005_V1_2008-10-14_denoised.nii',
    'E005_V2_2009-10-30_denoised.nii',
    'E005_V3_2010-12-16_denoised.nii',
    'E005_V4_2011-11-09_denoised.nii',
    'E005_V5_2013-02-13_denoised.nii',
    'E006_V1_2008-11-06_denoised.nii',
    'E006_V2_2009-10-30_denoised.nii',
    'E006_V3_2010-11-17_denoised.nii',
    'E006_V4_2011-12-14_denoised.nii',
    'E006_V5_2013-02-13_denoised.nii',
    'E008_V1_2008-10-28_denoised.nii',
    'E010_V1_2008-10-28_denoised.nii',
    'E010_V2_2009-11-10_denoised.nii',
    'E010_V3_2010-12-01_denoised.nii',
    'E010_V4_2011-12-13_denoised.nii',
    'E010_V5_2013-04-09_denoised.nii',
    'E011_V1_2008-11-04_denoised.nii',
    'E011_V2_2009-10-06_denoised.nii',
    'E011_V3_2010-09-03_denoised.nii',
    'E011_V5_2013-07-25_denoised.nii',
    'E013_V1_2008-11-12_denoised.nii',
    'E013_V2_2009-10-20_denoised.nii',
    'E013_V3_2010-12-08_denoised.nii',
    'E013_V4_2011-09-28_denoised.nii',
    'E013_V5_2012-11-08_denoised.nii',
    'E014_V1_2008-11-24_denoised.nii',
    'E014_V2_2010-01-14_denoised.nii',
    'E014_V3_2010-10-01_denoised.nii',
    'E014_V4_2011-11-01_denoised.nii',
    'E015_V1_2008-11-24_denoised.nii',
    'E015_V2_2009-09-29_denoised.nii',
    'E015_V3_2010-10-01_denoised.nii',
    'E015_V4_2011-11-01_denoised.nii',
    'E016_V1_2008-12-22_denoised.nii',
    'E016_V2_2010-01-04_denoised.nii',
    'E016_V3_2010-11-10_denoised.nii',
    'E016_V4_2011-09-14_denoised.nii',
    'E016_V5_2012-12-13_denoised.nii',
    'E017_V1_2008-11-14_denoised.nii',
    'E017_V2_2009-11-03_denoised.nii',
    'E017_V3_2011-01-11_denoised.nii',
    'E017_V4_2011-12-14_denoised.nii',
    'E017_V5_2013-02-12_denoised.nii',
    'E018_V1_2008-12-05_denoised.nii',
    'E019_V1_2008-11-18_denoised.nii',
    'E019_V2_2010-01-05_denoised.nii',
    'E019_V3_2011-01-25_denoised.nii',
    'E019_V4_2011-12-16_denoised.nii',
    'E019_V4_2012-02-01_denoised.nii',
    'E019_V5_2013-01-31_denoised.nii',
    'E020_V1_2008-11-18_denoised.nii',
    'E020_V2_2009-10-27_denoised.nii',
    'E020_V3_2010-12-21_denoised.nii',
    'E020_V4_2012-02-16_denoised.nii',
    'E020_V5_2012-10-11_denoised.nii',
    'E021_V1_2008-11-25_denoised.nii',
    'E021_V2_2009-12-22_denoised.nii',
    'E021_V3_2010-12-01_denoised.nii',
    'E022_V1_2008-11-25_denoised.nii',
    'E022_V2_2010-01-08_denoised.nii',
    'E022_V3_2010-12-08_denoised.nii',
    'E022_V4_2011-12-07_denoised.nii',
    'E023_V1_2008-11-21_denoised.nii',
    'E023_V2_2009-09-18_denoised.nii',
    'E024_V1_2008-12-29_denoised.nii',
    'E024_V2_2010-01-26_denoised.nii',
    'E027_V1_2009-01-09_denoised.nii',
    'E027_V2_2010-02-02_denoised.nii',
    'E027_V3_2011-03-11_denoised.nii',
    'E027_V4_2012-03-15_denoised.nii',
    'E027_V5_2013-03-22_denoised.nii',
    'E029_V1_2008-12-22_denoised.nii',
    'E029_V2_2009-11-18_denoised.nii',
    'E029_V3_2010-12-14_denoised.nii',
    'E029_V4_2011-10-25_denoised.nii',
    'E029_V5_2013-01-08_denoised.nii',
    'E030_V1_2009-01-13_denoised.nii',
    'E030_V2_2009-12-09_denoised.nii',
    'E030_V3_2011-02-18_denoised.nii',
    'E030_V4_2011-11-07_denoised.nii',
    'E030_V5_2013-02-08_denoised.nii',
    'E031_V1_2009-01-13_denoised.nii',
    'E031_V2_2010-04-14_denoised.nii',
    'E031_V3_2011-04-07_denoised.nii',
    'E031_V4_2012-05-22_denoised.nii',
    'E031_V5_2013-11-19_denoised.nii',
    'E032_V1_2009-01-13_denoised.nii',
    'E032_V2_2010-01-08_denoised.nii',
    'E032_V3_2011-02-25_denoised.nii',
    'E032_V4_2012-02-03_denoised.nii',
    'E033_V1_2009-02-17_denoised.nii',
    'E033_V2_2010-03-12_denoised.nii',
    'E033_V3_2011-05-31_denoised.nii',
    'E033_V4_2012-04-20_denoised.nii',
    'E033_V5_2013-06-06_denoised.nii',
    'E034_V1_2009-01-14_denoised.nii',
    'E034_V2_2009-10-27_denoised.nii',
    'E034_V3_2011-03-08_denoised.nii',
    'E034_V5_2013-03-28_denoised.nii',
    'E035_V1_2009-01-20_denoised.nii',
    'E035_V2_2009-10-13_denoised.nii',
    'E035_V3_2011-03-09_denoised.nii',
    'E035_V4_2011-10-17_denoised.nii',
    'E035_V5_2013-06-25_denoised.nii',
    'E036_V1_2009-01-27_denoised.nii',
    'E036_V2_2009-12-15_denoised.nii',
    'E036_V3_2011-02-22_denoised.nii',
    'E036_V4_2011-11-02_denoised.nii',
    'E036_V5_2013-01-22_denoised.nii',
    'E037_V1_2009-01-27_denoised.nii',
    'E037_V2_2010-04-16_denoised.nii',
    'E037_V3_2011-07-27_denoised.nii',
    'E037_V4_2012-02-08_denoised.nii',
    'E037_V5_2013-03-07_denoised.nii',
    'E038_V1_2009-01-28_denoised.nii',
    'E038_V2_2009-12-04_denoised.nii',
    'E038_V3_2011-05-06_denoised.nii',
    'E038_V4_2012-04-10_denoised.nii',
    'E038_V5_2014-11-06_denoised.nii',
    'E039_V1_2009-02-12_denoised.nii',
    'E039_V2_2010-02-11_denoised.nii',
    'E040_V1_2009-02-04_denoised.nii',
    'E040_V2_2010-03-16_denoised.nii',
    'E041_V1_2009-02-05_denoised.nii',
    'E041_V2_2010-01-12_denoised.nii',
    'E041_V3_2011-03-01_denoised.nii',
    'E041_V4_2012-01-17_denoised.nii',
    'E041_V5_2013-03-12_denoised.nii',
    'E043_V1_2009-02-27_denoised.nii',
    'E043_V2_2010-01-29_denoised.nii',
    'E043_V3_2011-02-22_denoised.nii',
    'E043_V4_2012-04-18_denoised.nii',
    'E043_V5_2013-07-23_denoised.nii',
    'E044_V1_2009-02-11_denoised.nii',
    'E044_V2_2009-12-18_denoised.nii',
    'E044_V3_2011-03-01_denoised.nii',
    'E044_V4_2012-05-08_denoised.nii',
    'E045_V1_2009-02-23_denoised.nii',
    'E045_V2_2010-03-09_denoised.nii',
    'E045_V3_2011-03-31_denoised.nii',
    'E045_V4_2012-03-22_denoised.nii',
    'E045_V5_2013-04-30_denoised.nii',
    'E046_V1_2009-03-03_denoised.nii',
    'E046_V2_2010-03-16_denoised.nii',
    'E046_V3_2011-03-08_denoised.nii',
    'E046_V4_2012-07-10_denoised.nii',
    'E046_V5_2013-05-16_denoised.nii',
    'E047_V1_2009-02-26_denoised.nii',
    'E047_V2_2010-02-03_denoised.nii',
    'E048_V1_2009-03-05_denoised.nii',
    'E048_V2_2010-03-26_denoised.nii',
    'E048_V3_2011-06-28_denoised.nii',
    'E048_V4_2012-02-08_denoised.nii',
    'E048_V5_2013-06-05_denoised.nii',
    'E049_V1_2009-03-06_denoised.nii',
    'E049_V2_2010-06-22_denoised.nii',
    'E049_V3_2011-06-21_denoised.nii',
    'E049_V4_2012-03-20_denoised.nii',
    'E050_V1_2009-04-16_denoised.nii',
    'E050_V2_2010-02-19_denoised.nii',
    'E050_V3_2011-03-16_denoised.nii',
    'E050_V4_2012-04-25_denoised.nii',
    'E050_V5_2013-05-01_denoised.nii',
    'E051_V1_2009-04-16_denoised.nii',
    'E051_V2_2010-02-19_denoised.nii',
    'E051_V3_2011-03-16_denoised.nii',
    'E051_V4_2012-04-25_denoised.nii',
    'E051_V5_2013-05-01_denoised.nii',
    'E052_V1_2009-03-13_denoised.nii',
    'E052_V2_2010-04-20_denoised.nii',
    'E052_V3_2011-04-08_denoised.nii',
    'E052_V4_2012-03-02_denoised.nii',
    'E053_V1_2009-03-17_denoised.nii',
    'E053_V2_2009-12-04_denoised.nii',
    'E053_V3_2011-03-01_denoised.nii',
    'E053_V4_2012-01-10_denoised.nii',
    'E053_V5_2012-12-18_denoised.nii',
    'E054_V1_2009-03-24_denoised.nii',
    'E054_V2_2010-04-23_denoised.nii',
    'E054_V3_2011-04-29_denoised.nii',
    'E054_V4_2012-06-26_denoised.nii',
    'E054_V5_2013-06-04_denoised.nii',
    'E055_V1_2009-03-31_denoised.nii',
    'E055_V2_2010-05-20_denoised.nii',
    'E055_V3_2011-04-19_denoised.nii',
    'E055_V4_2012-05-15_denoised.nii',
    'E055_V5_2013-06-27_denoised.nii',
    'E056_V1_2009-04-01_denoised.nii',
    'E056_V2_2010-04-08_denoised.nii',
    'E056_V3_2011-04-26_denoised.nii',
    'E056_V4_2012-03-21_denoised.nii',
    'E056_V5_2013-06-14_denoised.nii',
    'E057_V1_2009-03-24_denoised.nii',
    'E057_V2_2010-04-06_denoised.nii',
    'E057_V3_2011-05-18_denoised.nii',
    'E057_V4_2012-04-10_denoised.nii',
    'E057_V5_2013-06-03_denoised.nii',
    'E058_V1_2009-04-23_denoised.nii',
    'E058_V2_2010-04-20_denoised.nii',
    'E058_V3_2011-04-06_denoised.nii',
    'E058_V4_2012-04-17_denoised.nii',
    'E058_V5_2013-04-02_denoised.nii',
    'E060_V1_2009-05-19_denoised.nii',
    'E060_V2_2010-07-02_denoised.nii',
    'E060_V3_2011-07-26_denoised.nii',
    'E062_V1_2009-04-07_denoised.nii',
    'E062_V2_2010-03-12_denoised.nii',
    'E062_V3_2011-05-31_denoised.nii',
    'E062_V4_2012-04-20_denoised.nii',
    'E062_V5_2013-06-06_denoised.nii',
    'E065_V1_2009-04-13_denoised.nii',
    'E065_V2_2009-12-23_denoised.nii',
    'E065_V3_2011-02-16_denoised.nii',
    'E065_V4_2012-01-18_denoised.nii',
    'E065_V5_2013-03-12_denoised.nii',
    'E067_V1_2009-04-21_denoised.nii',
    'E068_V1_2009-04-21_denoised.nii',
    'E069_V1_2009-05-01_denoised.nii',
    'E069_V2_2010-05-21_denoised.nii',
    'E069_V3_2011-06-15_denoised.nii',
    'E069_V4_2012-05-23_denoised.nii',
    'E069_V5_2013-07-09_denoised.nii',
    'E070_V1_2009-05-05_denoised.nii',
    'E070_V2_2010-05-26_denoised.nii',
    'E071_V1_2009-05-05_denoised.nii',
    'E071_V2_2010-06-25_denoised.nii',
    'E071_V3_2011-09-28_denoised.nii',
    'E072_V1_2009-05-12_denoised.nii',
    'E073_V1_2009-05-26_denoised.nii',
    'E073_V2_2010-05-12_denoised.nii',
    'E073_V3_2011-06-23_denoised.nii',
    'E073_V4_2012-06-12_denoised.nii',
    'E073_V5_2013-06-11_denoised.nii',
    'E074_V1_2009-05-12_denoised.nii',
    'E075_V1_2009-05-22_denoised.nii',
    'E075_V2_2010-05-11_denoised.nii',
    'E075_V3_2011-05-24_denoised.nii',
    'E075_V4_2012-06-26_denoised.nii',
    'E075_V5_2013-05-14_denoised.nii',
    'E076_V1_2009-05-29_denoised.nii',
    'E076_V2_2010-06-14_denoised.nii',
    'E076_V3_2011-05-25_denoised.nii',
    'E076_V4_2012-06-27_denoised.nii',
    'E076_V5_2013-09-27_denoised.nii',
    'E077_V1_2009-05-19_denoised.nii',
    'E077_V2_2010-06-18_denoised.nii',
    'E077_V3_2011-09-07_denoised.nii',
    'E077_V4_2012-09-05_denoised.nii',
    'E077_V5_2013-08-27_denoised.nii',
    'E078_V1_2009-05-20_denoised.nii',
    'E078_V2_2010-06-11_denoised.nii',
    'E078_V3_2011-10-07_denoised.nii',
    'E078_V5_2013-08-19_denoised.nii',
    'E079_V1_2009-05-26_denoised.nii',
    'E079_V2_2010-07-07_denoised.nii',
    'E080_V1_2009-06-18_denoised.nii',
    'E080_V2_2010-08-02_denoised.nii',
    'E080_V3_2011-12-21_denoised.nii',
    'E080_V5_2013-11-04_denoised.nii',
    'E081_V1_2009-06-02_denoised.nii',
    'E081_V2_2010-06-09_denoised.nii',
    'E081_V3_2011-08-31_denoised.nii',
    'E081_V4_2012-09-26_denoised.nii',
    'E081_V5_2013-10-01_denoised.nii',
    'E082_V1_2009-06-02_denoised.nii',
    'E082_V2_2010-06-15_denoised.nii',
    'E082_V3_2011-06-14_denoised.nii',
    'E082_V4_2012-08-14_denoised.nii',
    'E082_V5_2013-10-01_denoised.nii',
    'E084_V1_2009-06-09_denoised.nii',
    'E084_V2_2010-10-27_denoised.nii',
    'E085_V1_2009-07-13_denoised.nii',
    'E085_V2_2010-06-15_denoised.nii',
    'E085_V3_2011-08-02_denoised.nii',
    'E085_V4_2013-02-27_denoised.nii',
    'E085_V5_2013-08-21_denoised.nii',
    'E086_V1_2009-06-23_denoised.nii',
    'E086_V2_2010-06-29_denoised.nii',
    'E086_V3_2011-08-10_denoised.nii',
    'E086_V4_2012-08-22_denoised.nii',
    'E086_V5_2013-10-29_denoised.nii',
    'E088_V1_2009-06-16_denoised.nii',
    'E088_V2_2010-07-30_denoised.nii',
    'E088_V3_2011-09-30_denoised.nii',
    'E088_V4_2012-10-10_denoised.nii',
    'E088_V5_2013-11-13_denoised.nii',
    'E089_V1_2009-06-16_denoised.nii',
    'E089_V2_2010-07-30_denoised.nii',
    'E089_V3_2011-09-30_denoised.nii',
    'E089_V4_2012-10-10_denoised.nii',
    'E089_V5_2013-11-13_denoised.nii',
    'E090_V1_2009-06-11_denoised.nii',
    'E090_V2_2010-08-25_denoised.nii',
    'E090_V3_2011-07-07_denoised.nii',
    'E090_V5_2013-07-03_denoised.nii',
    'E092_V1_2009-07-17_denoised.nii',
    'E092_V2_2010-06-23_denoised.nii',
    'E092_V3_2011-06-28_denoised.nii',
    'E092_V4_2012-09-11_denoised.nii',
    'E092_V5_2013-10-29_denoised.nii',
    'E093_V1_2009-07-24_denoised.nii',
    'E093_V2_2010-07-27_denoised.nii',
    'E094_V1_2009-07-09_denoised.nii',
    'E094_V2_2010-07-28_denoised.nii',
    'E094_V3_2011-06-23_denoised.nii',
    'E095_V1_2009-07-08_denoised.nii',
    'E095_V2_2010-11-01_denoised.nii',
    'E095_V5_2015-02-25_denoised.nii',
    'E096_V1_2009-07-07_denoised.nii',
    'E096_V2_2010-07-26_denoised.nii',
    'E096_V3_2011-09-20_denoised.nii',
    'E097_V1_2009-09-11_denoised.nii',
    'E097_V2_2010-10-29_denoised.nii',
    'E097_V4_2012-08-23_denoised.nii',
    'E097_V5_2013-10-25_denoised.nii',
    'E098_V1_2009-07-15_denoised.nii',
    'E098_V2_2010-06-25_denoised.nii',
    'E098_V3_2011-06-07_denoised.nii',
    'E098_V4_2012-09-18_denoised.nii',
    'E098_V5_2013-07-30_denoised.nii',
    'E099_V1_2009-07-17_denoised.nii',
    'E099_V2_2010-06-04_denoised.nii',
    'E099_V3_2011-05-12_denoised.nii',
    'E099_V4_2012-07-06_denoised.nii',
    'E099_V5_2013-06-25_denoised.nii',
    'E100_V1_2009-07-21_denoised.nii',
    'E101_V1_2009-07-21_denoised.nii',
    'E102_V1_2009-07-21_denoised.nii',
    'E102_V2_2010-07-06_denoised.nii',
    'E102_V3_2011-08-10_denoised.nii',
    'E105_V1_2009-07-28_denoised.nii',
    'E105_V2_2010-08-25_denoised.nii',
    'E105_V3_2011-10-26_denoised.nii',
    'E105_V5_2013-12-10_denoised.nii',
    'E107_V1_2009-08-21_denoised.nii',
    'E107_V2_2010-10-05_denoised.nii',
    'E107_V3_2011-08-24_denoised.nii',
    'E109_V1_2009-08-28_denoised.nii',
    'E109_V2_2010-10-29_denoised.nii',
    'E111_V1_2009-09-22_denoised.nii',
    'E111_V2_2010-10-26_denoised.nii',
    'E111_V3_2011-10-25_denoised.nii',
    'E111_V4_2013-02-01_denoised.nii',
    'E111_V5_2013-10-28_denoised.nii',
    'E112_V1_2009-10-06_denoised.nii',
    'E112_V2_2010-10-27_denoised.nii',
    'E112_V3_2011-11-16_denoised.nii',
    'E112_V4_2013-02-04_denoised.nii',
    'E112_V5_2013-12-04_denoised.nii',
    'E113_V1_2009-09-04_denoised.nii',
    'E113_V2_2010-08-06_denoised.nii',
    'E113_V3_2011-07-12_denoised.nii',
    'E113_V5_2013-07-02_denoised.nii',
    'E114_V1_2009-09-17_denoised.nii',
    'E114_V2_2010-11-12_denoised.nii',
    'E115_V1_2009-10-21_denoised.nii',
    'E115_V2_2010-10-13_denoised.nii',
    'E115_V3_2011-09-16_denoised.nii',
    'E115_V5_2013-12-17_denoised.nii',
    'E116_V1_2009-10-23_denoised.nii',
    'E116_V2_2010-10-19_denoised.nii',
    'E117_V1_2009-08-10_denoised.nii',
    'E117_V2_2010-11-22_denoised.nii',
    'E117_V3_2011-11-30_denoised.nii',
    'E118_V1_2009-12-15_denoised.nii',
    'E118_V2_2010-10-27_denoised.nii',
    'E118_V3_2011-12-08_denoised.nii',
    'E120_V1_2009-11-10_denoised.nii',
    'E120_V2_2010-11-10_denoised.nii',
    'E122_V1_2010-01-13_denoised.nii',
    'E122_V2_2011-03-23_denoised.nii',
    'E122_V3_2012-01-25_denoised.nii',
    'E122_V4_2013-01-30_denoised.nii',
    'E122_V5_2014-03-11_denoised.nii',
    'E123_V1_2009-10-19_denoised.nii',
    'E123_V2_2010-11-05_denoised.nii',
    'E123_V3_2011-12-02_denoised.nii',
    'E123_V4_2013-04-02_denoised.nii',
    'E123_V5_2014-02-24_denoised.nii',
    'E124_V1_2010-01-19_denoised.nii',
    'E124_V2_2011-02-15_denoised.nii',
    'E124_V5_2015-02-02_denoised.nii',
    'E125_V1_2010-01-19_denoised.nii',
    'E125_V2_2011-02-15_denoised.nii',
    'E126_V1_2010-02-09_denoised.nii',
    'E126_V4_2013-02-12_denoised.nii',
    'E127_V1_2009-12-18_denoised.nii',
    'E127_V2_2011-06-13_denoised.nii',
    'E127_V3_2012-04-04_denoised.nii',
    'E127_V4_2013-05-07_denoised.nii',
    'E127_V5_2014-03-18_denoised.nii',
    'E128_V1_2009-12-22_denoised.nii',
    'E128_V2_2011-01-05_denoised.nii',
    'E128_V3_2012-01-27_denoised.nii',
    'E128_V4_2013-05-31_denoised.nii',
    'E128_V5_2014-11-21_denoised.nii',
    'E132_V1_2010-02-10_denoised.nii',
    'E132_V2_2011-02-09_denoised.nii',
    'E132_V3_2012-02-08_denoised.nii',
    'E132_V4_2013-02-20_denoised.nii',
    'E133_V1_2010-02-10_denoised.nii',
    'E133_V2_2011-02-16_denoised.nii',
    'E134_V1_2010-03-24_denoised.nii',
    'E134_V2_2011-02-23_denoised.nii',
    'E134_V3_2012-05-29_denoised.nii',
    'E136_V1_2009-11-13_denoised.nii',
    'E136_V2_2011-01-05_denoised.nii',
    'E136_V3_2012-02-22_denoised.nii',
    'E136_V4_2013-05-10_denoised.nii',
    'E136_V5_2014-04-22_denoised.nii',
    'E137_V1_2010-04-07_denoised.nii',
    'E137_V4_2013-10-07_denoised.nii',
    'E141_V1_2010-04-05_denoised.nii',
    'E141_V2_2011-04-22_denoised.nii',
    'E141_V3_2012-05-18_denoised.nii',
    'E141_V4_2013-04-30_denoised.nii',
    'E141_V5_2014-12-05_denoised.nii',
    'E142_V1_2010-04-20_denoised.nii',
    'E143_V1_2010-04-30_denoised.nii',
    'E143_V2_2011-04-01_denoised.nii',
    'E143_V3_2012-06-26_denoised.nii',
    'E143_V4_2013-05-08_denoised.nii',
    'E143_V5_2014-10-24_denoised.nii',
    'E147_V1_2010-06-01_denoised.nii',
    'E147_V2_2011-06-29_denoised.nii',
    'E147_V3_2012-06-22_denoised.nii',
    'E147_V4_2013-06-10_denoised.nii',
    'E147_V5_2014-11-25_denoised.nii',
    'E150_V1_2010-06-18_denoised.nii',
    'E150_V2_2011-05-16_denoised.nii',
    'E151_V1_2010-06-22_denoised.nii',
    'E152_V1_2010-05-11_denoised.nii',
    'E152_V2_2011-08-26_denoised.nii',
    'E152_V3_2012-10-24_denoised.nii',
    'E152_V4_2013-08-27_denoised.nii',
    'E152_V5_2014-10-15_denoised.nii',
    'E153_V1_2010-07-30_denoised.nii',
    'E153_V2_2011-05-25_denoised.nii',
    'E153_V3_2012-05-18_denoised.nii',
    'E153_V5_2014-10-07_denoised.nii',
    'E154_V1_2010-08-27_denoised.nii',
    'E154_V2_2011-09-09_denoised.nii',
    'E155_V1_2010-09-01_denoised.nii',
    'E155_V2_2011-08-19_denoised.nii',
    'E155_V3_2012-11-08_denoised.nii',
    'E155_V4_2013-09-10_denoised.nii',
    'E155_V5_2014-10-22_denoised.nii',
    'E156_V1_2010-08-19_denoised.nii',
    'E156_V2_2011-08-26_denoised.nii',
    'E156_V3_2012-10-24_denoised.nii',
    'E156_V4_2013-08-27_denoised.nii',
    'E156_V5_2014-10-15_denoised.nii',
    'E158_V1_2010-09-21_denoised.nii',
    'E158_V2_2011-11-29_denoised.nii',
    'E158_V3_2012-12-05_denoised.nii',
    'E158_V4_2014-02-25_denoised.nii',
    'E158_V5_2015-02-17_denoised.nii',
    'E159_V1_2010-10-12_denoised.nii',
    'E159_V3_2012-12-03_denoised.nii',
    'E159_V4_2013-10-07_denoised.nii',
    'E159_V5_2014-10-09_denoised.nii',
    'E161_V1_2010-12-01_denoised.nii',
    'E161_V2_2011-08-05_denoised.nii',
    'E163_V1_2010-11-15_denoised.nii',
    'E163_V2_2011-11-16_denoised.nii',
    'E163_V3_2013-01-16_denoised.nii',
    'E163_V4_2013-11-12_denoised.nii',
    'E163_V5_2015-02-24_denoised.nii',
    'E164_V1_2010-11-23_denoised.nii',
    'E164_V4_2014-02-18_denoised.nii',
    'E165_V1_2010-08-16_denoised.nii',
    'E165_V3_2013-04-29_denoised.nii',
    'E166_V1_2010-11-02_denoised.nii',
    'E166_V2_2012-01-11_denoised.nii',
    'E166_V3_2013-04-30_denoised.nii',
    'E166_V4_2014-05-20_denoised.nii',
    'E166_V5_2015-05-12_denoised.nii',
    'E168_V1_2010-12-13_denoised.nii',
    'E168_V2_2012-08-14_denoised.nii',
    'E168_V3_2013-05-07_denoised.nii',
    'E168_V4_2014-10-10_denoised.nii',
    'E168_V5_2015-04-28_denoised.nii',
    'E169_V1_2010-11-23_denoised.nii',
    'E169_V2_2012-01-18_denoised.nii',
    'E169_V3_2012-12-11_denoised.nii',
    'E169_V4_2013-12-03_denoised.nii',
    'E169_V5_2015-04-08_denoised.nii',
    'E171_V1_2010-09-28_denoised.nii',
    'E171_V2_2012-03-29_denoised.nii',
    'E172_V1_2010-12-17_denoised.nii',
    'E172_V2_2012-02-22_denoised.nii',
    'E172_V3_2013-07-09_denoised.nii',
    'E172_V4_2014-05-13_denoised.nii',
    'E172_V5_2015-05-26_denoised.nii',
    'E173_V1_2010-12-13_denoised.nii',
    'E174_V1_2011-04-18_denoised.nii',
    'E174_V2_2012-08-31_denoised.nii',
    'E174_V4_2014-11-20_denoised.nii',
    'E176_V1_2011-04-18_denoised.nii',
    'E177_V1_2011-04-05_denoised.nii',
    'E177_V2_2012-06-12_denoised.nii',
    'E177_V5_2015-10-02_denoised.nii',
    'E179_V1_2011-04-12_denoised.nii',
    'E179_V2_2012-05-29_denoised.nii',
    'E179_V3_2013-05-30_denoised.nii',
    'E179_V4_2014-11-12_denoised.nii',
    'E179_V5_2015-06-01_denoised.nii',
    'E181_V1_2011-05-16_denoised.nii',
    'E181_V2_2012-10-26_denoised.nii',
    'E181_V5_2015-06-10_denoised.nii',
    'E182_V1_2011-04-27_denoised.nii',
    'E182_V2_2012-06-28_denoised.nii',
    'E182_V3_2013-05-28_denoised.nii',
    'E182_V4_2014-11-24_denoised.nii',
    'E182_V5_2015-10-06_denoised.nii',
    'E183_V1_2011-03-24_denoised.nii',
    'E183_V2_2012-08-14_denoised.nii',
    'E183_V3_2013-10-01_denoised.nii',
    'E183_V4_2015-01-14_denoised.nii',
    'E183_V5_2015-09-29_denoised.nii',
    'E185_V1_2011-05-11_denoised.nii',
    'E185_V2_2012-04-26_denoised.nii',
    'E185_V3_2013-07-30_denoised.nii',
    'E185_V5_2015-07-02_denoised.nii',
    'E186_V1_2011-06-22_denoised.nii',
    'E186_V2_2012-06-15_denoised.nii',
    'E186_V4_2014-10-29_denoised.nii',
    'E187_V1_2011-05-03_denoised.nii',
    'E187_V2_2012-07-25_denoised.nii',
    'E187_V3_2013-05-07_denoised.nii',
    'E187_V4_2014-10-24_denoised.nii',
    'E187_V5_2015-11-09_denoised.nii',
    'E189_V1_2010-12-02_denoised.nii',
    'E189_V2_2012-09-12_denoised.nii',
    'E189_V3_2013-05-13_denoised.nii',
    'E189_V4_2014-10-15_denoised.nii',
    'E189_V5_2015-09-21_denoised.nii',
    'E190_V1_2011-06-08_denoised.nii',
    'E191_V1_2011-05-10_denoised.nii',
    'E191_V2_2012-12-14_denoised.nii',
    'E191_V3_2013-10-14_denoised.nii',
    'E191_V4_2014-10-21_denoised.nii',
    'E191_V5_2016-02-22_denoised.nii',
    'E193_V1_2011-07-01_denoised.nii',
    'E193_V3_2013-08-28_denoised.nii',
    'E193_V4_2014-10-13_denoised.nii',
    'E193_V5_2015-09-22_denoised.nii',
    'E195_V1_2011-06-29_denoised.nii',
    'E197_V1_2011-05-06_denoised.nii',
    'E197_V2_2012-08-03_denoised.nii',
    'E201_V1_2011-07-06_denoised.nii',
    'E201_V2_2012-08-01_denoised.nii',
    'E201_V3_2013-06-17_denoised.nii',
    'E201_V4_2014-10-08_denoised.nii',
    'E201_V5_2015-06-02_denoised.nii',
    'E203_V1_2011-07-01_denoised.nii',
    'E203_V2_2012-08-29_denoised.nii',
    'E203_V3_2013-10-23_denoised.nii',
    'E203_V4_2014-10-13_denoised.nii',
    'E203_V5_2015-06-08_denoised.nii',
    'E206_V1_2011-07-11_denoised.nii',
    'E206_V2_2012-11-07_denoised.nii',
    'E206_V3_2013-09-18_denoised.nii',
    'E210_V1_2011-08-25_denoised.nii',
    'E210_V3_2013-11-08_denoised.nii',
    'E210_V4_2014-10-21_denoised.nii',
    'E210_V5_2015-05-28_denoised.nii',
    'E211_V1_2011-08-18_denoised.nii',
    'E212_V1_2011-08-05_denoised.nii',
    'E214_V1_2011-11-07_denoised.nii',
    'E214_V2_2012-12-04_denoised.nii',
    'E216_V1_2012-01-25_denoised.nii',
    'E216_V2_2013-04-26_denoised.nii',
    'E216_V5_2016-01-15_denoised.nii',
    'E220_V1_2012-03-09_denoised.nii',
    'E220_V2_2013-05-09_denoised.nii',
    'E220_V3_2014-04-08_denoised.nii',
    'E220_V5_2016-02-09_denoised.nii',
    'E222_V1_2012-02-29_denoised.nii',
    'E222_V2_2013-03-25_denoised.nii',
    'E222_V3_2014-03-17_denoised.nii',
    'E222_V4_2015-05-22_denoised.nii',
    'E222_V5_2016-01-22_denoised.nii',
    'E301_V1_2010-04-01_denoised.nii',
    'E302_V1_2010-05-19_denoised.nii',
    'E304_V1_2010-06-15_denoised.nii',
    'E305_V1_2010-06-29_denoised.nii',
    'E306_V1_2010-08-11_denoised.nii',
    'E308_V1_2010-09-14_denoised.nii',
    'E309_V1_2010-10-12_denoised.nii',
    'E310_V1_2010-10-12_denoised.nii',
    'E311_V1_2011-03-16_denoised.nii',
    'E313_V1_2010-12-20_denoised.nii',
    'E315_V1_2011-03-02_denoised.nii',
    'E316_V1_2011-03-09_denoised.nii',
    'E317_V1_2011-03-01_denoised.nii',
    'E318_V1_2011-04-08_denoised.nii',
    'E319_V1_2011-06-20_denoised.nii',
    'E321_V1_2011-06-22_denoised.nii',
    'E322_V1_2011-09-26_denoised.nii',
    'E323_V1_2011-07-11_denoised.nii',
    'E324_V1_2012-04-11_denoised.nii',
    'E325_V1_2012-05-08_denoised.nii',
    'E329_V1_2013-09-09_denoised.nii',
    'E330_V1_2013-08-22_denoised.nii',
    'E331_V1_2013-09-18_denoised.nii',
    'E333_V1_2013-12-03_denoised.nii',
    'E334_V1_2013-11-25_denoised.nii',
    'E336_V1_2014-04-01_denoised.nii',
    'E337_V1_2014-03-12_denoised.nii',
    'E338_V1_2014-10-08_denoised.nii',
    'E339_V1_2014-10-13_denoised.nii',
    'E340_V1_2014-10-09_denoised.nii',
    'E341_V1_2014-10-29_denoised.nii',
    'E343_V1_2014-12-18_denoised.nii',
    'E344_V1_2015-02-03_denoised.nii',
    'E345_V1_2015-02-24_denoised.nii',
    'E346_V1_2015-03-03_denoised.nii',
    'E347_V1_2015-03-10_denoised.nii',
    'E349_V1_2015-03-11_denoised.nii',
    'E350_V1_2015-03-24_denoised.nii'
    ]

for i in filename:
    file_name = i[:7]
    
    with open(file_name + '.sh', 'w') as script_file:
    
        script_file.write('#!/bin/sh\n')
        script_file.write(f'#SBATCH -J {file_name}\n')
        script_file.write('#SBATCH -p general\n')
        script_file.write('#SBATCH -o %j.txt\n')
        script_file.write('#SBATCH -e %j.err\n')
        script_file.write('#SBATCH --mail-type=END,FAIL\n')
        script_file.write('#SBATCH --mail-user=nsangani@iu.edu\n')
        script_file.write('#SBATCH --nodes=1\n')
        script_file.write('#SBATCH --ntasks-per-node=16\n')
        script_file.write('#SBATCH --time=24:00:00\n')
        script_file.write('#SBATCH --mem=15gb\n')
        script_file.write('#SBATCH -A general\n\n')
        
        script_file.write('module load freesurfer/7.4.1\n')
        
        script_file.write('recon-all ' + i)

    
# Open the 'superscript.txt' file in append mode
with open('superscript.sh', 'a') as script_file:
    # Loop through each filename in the list
    for i in filename:
        # Extract the first 7 characters and add '.txt'
        file_name = i[:7] + '.txt'
        
        # Write the filename to the file, preceded by 'sbatch ' and followed by a newline
        script_file.write('sbatch ' + file_name + '\n')
        

PET_subject = [
    'E001'
    'E004'
    'E005'
    'E006'
    'E010'
    'E011'
    'E013'
    'E017'
    'E019'
    'E020'
    'E031'
    'E033'
    'E034'
    'E037'
    'E038'
    'E039'
    'E045'
    'E047'
    'E049'
    'E050'
    'E051'
    'E053'
    'E054'
    'E057'
    'E062'
    'E065'
    'E069'
    'E073'
    'E075'
    'E080'
    'E081'
    'E082'
    'E085'
    'E086'
    'E088'
    'E089'
    'E092'
    'E098'
    'E111'
    'E112'
    'E122'
    'E123'
    'E124'
    'E127'
    'E128'
    'E136'
    'E141'
    'E143'
    'E147'
    'E152'
    'E153'
    'E155'
    'E156'
    'E158'
    'E159'
    'E168'
    'E169'
    'E172'
    'E179'
    'E181'
    'E183'
    'E185'
    'E186'
    'E193'
    'E201'
    'E203'
    'E210'
    'E216'
    'E220'
    'E222'
    ]
        
# Open the dcm2nii file in append mode
with open('dcm2nii_pet_IMAGENE.sh', 'a') as script_file:
    # Loop through each filename in the list
    for i in PET_subject:
        
        # Write the dcm2niix to filename
        script_file.write('dcm2niix ' + i + '\n')
            
        