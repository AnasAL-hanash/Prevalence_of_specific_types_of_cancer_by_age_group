import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# الخطوة 1: إنشاء بيانات باستخدام numpy
# فئات عمرية
ages = np.array(['0-18', '19-35', '36-50', '51-65', '65+'])

# نسب أنواع السرطان المختلفة لكل فئة عمرية (قيم افتراضية)
cancer_rates = np.array([
    [0.1, 0.2, 0.1, 0.3, 0.05],  # سرطان الثدي
    [0.05, 0.15, 0.2, 0.25, 0.1],  # سرطان القولون
    [0.02, 0.05, 0.1, 0.2, 0.3],  # سرطان الرئة
])

# أسماء السرطانات
cancer_types = ['Breast Cancer', 'Colon Cancer', 'Lung Cancer']

# الخطوة 2: تنظيم البيانات باستخدام pandas
df = pd.DataFrame(cancer_rates.T, columns=cancer_types, index=ages)
print("DataFrame:\n", df)

# الخطوة 3: رسم البيانات باستخدام matplotlib
df.plot(kind='bar', figsize=(10, 6))
plt.title('Cancer Rates by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Cancer Rate')
plt.xticks(rotation=0)
plt.legend(title='Cancer Type')
plt.show()