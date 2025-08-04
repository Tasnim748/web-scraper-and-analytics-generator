# analysis.py

def basic_analysis(df, numeric_fields=None, text_fields=None):
    numeric_fields = numeric_fields or []
    text_fields = text_fields or []
    
    analysisResult = {
        'numeric': [],
        'text': []
    }
    for field in numeric_fields:
        if field in df.columns:
            avg = df[field].mean()
            analysisResult['numeric'].append(f"Average {field}: {avg:.2f}")
    for field in text_fields:
        if field in df.columns:
            most_common = df[field].mode()[0]
            analysisResult['text'].append(f"Most common {field}: {most_common}")

    return analysisResult