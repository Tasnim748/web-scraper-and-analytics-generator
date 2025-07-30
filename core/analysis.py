# analysis.py

def basic_analysis(df, numeric_fields=None, text_fields=None):
    numeric_fields = numeric_fields or []
    text_fields = text_fields or []
    for field in numeric_fields:
        if field in df.columns:
            avg = df[field].mean()
            print(f"Average {field}: {avg:.2f}")
    for field in text_fields:
        if field in df.columns:
            most_common = df[field].mode()[0]
            print(f"Most common {field}: {most_common}")