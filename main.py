import pandas as pd

# Əvvəlcə verilənləri yükləyirik
file_path = '/content/Raman 2001_Quadrupole deformation data.xlsx'
excel_data = pd.ExcelFile(file_path)

excel_data.sheet_names

# İlk vərəqdən məlumatları yükləyirik
sheet_data = excel_data.parse('Sheet1')

# Onun strukturunu və məzmununu başa düşmək üçün verilənlər toplusunun ilk bir neçə sətirini göstəririk
sheet_data.head(), sheet_data.info()

# Çatışmayan dəyərləri təhlil edirik
missing_summary = sheet_data.isnull().sum()

# Hər sütun üçün çatışmayan dəyərlərin faizini hesablayırıq
missing_percentage = (missing_summary / len(sheet_data)) * 100

missing_info = pd.DataFrame({
    'Missing Values': missing_summary,
    'Percentage (%)': missing_percentage
}).sort_values(by='Missing Values', ascending=False)

missing_info

# Lazım olan kitabxanaları yükəyirik
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import pandas as pd

# Proqnozlaşdırmaq üçün sütunları qeyd edirik
target_columns = [
    'B(E2) (e2b2)', 'B(E2)_err (e2b2)', 'to (ps)', 'to_error (ps)', 'β2', 'β2_error', 
    'β/β(sp)', 'β/β(sp_ error)', 'Q0(b)', 'Q0(b)_error', 'E(keV)', 'E_error(keV)'
]

# Proqnozlaşdırma üçün məlumatlar
feature_columns = ['Z', 'N', 'A']  
imputer = SimpleImputer(strategy='mean')

# Verilənləri yeni cədvələ kopyalayırıq
updated_data = sheet_data.copy()

# Çatışmayan dəyərləri olan hər bir hədəfi sütun üzərində axtarırıq
for target in target_columns:
    # Cari hədəf üçün məlumat hazırlayırıq
    target_data = updated_data.dropna(subset=[target])
    # Xüsusiyyətlər
    X = target_data[feature_columns] 
    # Hədəf dəyərləri
    y = target_data[target]           

    # Çatışmayan dəyərləri daxil edirik
    X = imputer.fit_transform(X)
    
    # Məlumatları təlim və sınaq dəstlərinə bölürük
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Random Forest modeli işə salırıq
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Çatışmayan dəyərləri proqnozlaşdırırıq
    missing_rows = updated_data[updated_data[target].isnull()]
    if not missing_rows.empty:
        X_missing = imputer.transform(missing_rows[feature_columns]) 
        predictions = model.predict(X_missing)

        # Məlumatların proqnozlaşdırıldığı yeni cədvəli doldururq
        updated_data.loc[updated_data[target].isnull(), target] = predictions

# Yenilənmiş məlumarı yadda saxlayırıq
updated_data.to_excel('complete_dataset_with_predictions.xlsx', index=False)
print("Predicted all missing values. Updated dataset saved as 'complete_dataset_with_predictions.xlsx'.")
