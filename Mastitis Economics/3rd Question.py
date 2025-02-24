import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\adeolu.adekunle\OneDrive - Texas A&M AgriLife\Desktop\Git-tutorial\Decision-Science-for-Sustainable-Livestock-Systems_Module-2\3_body_weight_01.csv')  

print(df.head())

# Heifer Parameters
HM = Heifer_multiplier = 1
H_BWT = Heifer_max_body_weight = 588
H_DM_E = DM_energy = 2.3

# Lactation 1 parameters
C1 = lactation_1_age_at_calving = 730
A1 = lactation_1_mature_live_weight = 600
Y1 = lactation_1_birth_weight = 42
K1 = lactation_1_growth_rate_parameter = 3.9
p1L1 = lactation_1_maximum_decrease_of_liveweight_during_lactation = 20
p2L1 = lactation_1_time_during_lacatation_with_the_minimum_live_weight = 65
p3L1 = lactation_1_pregnancy_parameter = 0.02
M1 = multiplier = 1

# Lactation 2 parameters
C2 = lactation_1_age_at_calving = 1200
A2 = lactation_1_mature_live_weight = 640
Y2 = lactation_1_birth_weight = 42
K2 = lactation_1_growth_rate_parameter = 6
p1L2 = lactation_1_maximum_decrease_of_liveweight_during_lactation = 40
p2L2 = lactation_1_time_during_lacatation_with_the_minimum_live_weight = 70
p3L2 = lactation_1_pregnancy_parameter = 0.02
M2 = multiplier = 1

# woodmilk curve lactation 1
am1 = 15.6862
bm1 = 0.2081
cm1 = 0.0020
dm1 = 1
em1 = 0

# woodmilk curve lactation 2
am2 = 24.1895
bm2 = 0.1783
cm2 = 0.0031
dm2 = 1
em2 = 0

# woodfat curve lactation 1
af1 = 0.7131
bf1 = 0.1743
cf1 = 0.00183
df1 = 1
ef1 = 0

# woodfat curve lactation 2
af2 = 1.0558
bf2 = 0.1456
cf2 = 0.00283
df2 = 1
ef2 = 0

# woodprotein curve lactation 1
ap1 = 0.5209
bp1 = 0.1818
cp1 = 0.00190
dp1 = 1
ep1 = 0

# woodprotein curve lactation 2
ap2 = 0.8257
bp2 = 0.1464
cp2 = 0.00283
dp2 = 1
ep2 = 0

# somatic cell count lactation 1
ac1 = 1.9800
bc1 = -0.0030
cc1 = 0
dc1 = 16.8830
ec1 = 2
fc1 = 0

# somatic cell count lactation 2
ac2 = 2.5070
bc2 = -0.0040
cc2 = 0
dc2 = 8.9800
ec2 = 1
fc2 = 0

# Solution for the body weight

# adding new row for heifers
df['Predicted_BWT_Heifer'] = np.minimum(np.maximum(50, 28.115 + 6.2692 * df["week"] - 0.0117 * df["week"] ** 2), H_BWT) * HM
print(df.head())

# adding a new row for the Lactation 1
df['Lactation 1 Age'] = df['day'] + C1

df["Function (Lactation 1 Age)"] = (A1*(1-(1-(Y1/A1)**(1/3)) * np.exp(-K1 / 1000 * df["Lactation 1 Age"])) ** 3)

df["Function (Lactation 1 Lactation)"] = (p1L1/p2L1*df['day']*np.exp(1-df['day']/p2L1))

df["Predicted_BWT_Lact_1"] = (df["Function (Lactation 1 Age)"]- df["Function (Lactation 1 Lactation)"])*M1

print(df.head())

# adding a new row for the Lactation 2+
df['Lactation 2 Age'] = df['day'] + C2

df["Function (Lactation 2 Age)"] = (A2*(1-(1-(Y2/A2)**(1/3)) * np.exp(-K2 / 1000 * df["Lactation 2 Age"])) ** 3)

df["Function (Lactation 2 Lactation)"] = (p1L2/p2L2*df['day']*np.exp(1-df['day']/p2L2))

df["Predicted_BWT_Lact_2"] = (df["Function (Lactation 2 Age)"]- df["Function (Lactation 2 Lactation)"])*M2

print(df.head())


# Solution for the DMI

# adding new row for heifers
df['Predicted_DMI_Heifer'] = df['Predicted_BWT_Heifer'] **0.75 *(0.2435* H_DM_E -0.0466*H_DM_E ** 2 - 0.1128)/H_DM_E 
print(df.head())

# Solution for the woodfat curve
# Woodfat curve for the lactation 1
df["Predicted_milkfat_for_Lac_1"] = ((af1 * df['day'] ** bf1 * np.exp(-df['day'] * cf1)) + ef1) * df1
print(df["Predicted_milkfat_for_Lac_1"].head()) 

# Woodfat curve for the lactation 2
df["Predicted_milkfat_for_Lac_2"] = ((af2 * df['day'] ** bf2 * np.exp(-df['day'] * cf2)) + ef2) * df2
print(df["Predicted_milkfat_for_Lac_2"].head()) 

# Solution for the woodprotein curve
# Woodprotein curve for the lactation 1
df["Predicted_milkprotein_for_Lac_1"] = ((ap1 * df['day'] ** bp1 * np.exp(-df['day'] * cp1)) + ep1) * dp1
print(df["Predicted_milkprotein_for_Lac_1"].head()) 

# Woodprotein curve for the lactation 2
df["Predicted_milkprotein_for_Lac_2"] = ((ap2 * df['day'] ** bp2 * np.exp(-df['day'] * cp2)) + ep2) * dp2
print(df["Predicted_milkprotein_for_Lac_2"].head()) 


# adding a new row for animals in the Lactation 1 DMI
df["Predicted_DMI_Lac_1"] = (0.372 * (0.4 * df["Predicted_milk_yield_for_Lac_1"] + 15 * df["Predicted_milkfat_for_Lac_1"]) + 0.0968 * df["Predicted_BWT_Lact_1"] ** 0.75) * (1 - np.exp(-0.192 * (df["week"] + 3.67)))
print(df["Predicted_DMI_Lac_1"].head()) 

# adding a new row for animals in the Lactation 1 DMI
df["Predicted_DMI_Lac_2"] = (0.372 * (0.4 * df["Predicted_milk_yield_for_Lac_2"] + 15 * df["Predicted_milkfat_for_Lac_2"]) + 0.0968 * df["Predicted_BWT_Lact_2"] ** 0.75) * (1 - np.exp(-0.192 * (df["week"] + 3.67)))
print(df["Predicted_DMI_Lac_2"].head()) 

# Solution for the lactation/ woodmilk curve
# Woodmilk curve for the lactation 1
df["Predicted_milk_yield_for_Lac_1"] = ((am1 * df['day'] ** bm1 * np.exp(-df['day'] * cm1)) + em1) * dm1
print(df["Predicted_milk_yield_for_Lac_1"].head()) 

# Woodmilk curve for the lactation 2
df["Predicted_milk_yield_for_Lac_2"] = ((am2 * df['day'] ** bm2 * np.exp(-df['day'] * cm2)) + em2) * dm2
print(df["Predicted_milk_yield_for_Lac_2"].head()) 

# Solution for the Somatic Cell Count
# Somatic Cell Count for the lactation 1
df["Predicted_SCC_for_Lac_1"] = ((ac1-bc1 * df["week"] + cc1 * df["week"] ** 2 / 2+ dc1/df["week"]) + fc1) * ec1
print(df["Predicted_SCC_for_Lac_1"].head()) 

# Somatic Cell Count for the lactation 2
df["Predicted_SCC_for_Lac_2"] = ((ac2-bc2 * df["week"] + cc2 * df["week"] ** 2 / 2+ dc2/df["week"]) + fc2) * ec2
print(df["Predicted_SCC_for_Lac_2"].head())
