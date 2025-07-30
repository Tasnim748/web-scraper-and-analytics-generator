# visualize.py

import matplotlib.pyplot as plt

def plot_bar(df, x_field, y_field, title=None):
    if x_field not in df.columns or y_field not in df.columns:
        print(f"Fields {x_field} or {y_field} not found in DataFrame.")
        return
    plt.figure(figsize=(10,6))
    plt.bar(df[x_field], df[y_field])
    plt.xticks(rotation=45, ha='right')
    plt.xlabel(x_field.capitalize())
    plt.ylabel(y_field.capitalize())
    plt.title(title or f"{y_field.capitalize()} by {x_field.capitalize()}")
    plt.tight_layout()
    plt.show()

def plot_line(df, x_field, y_field, title=None):
    if x_field not in df.columns or y_field not in df.columns:
        print(f"Fields {x_field} or {y_field} not found in DataFrame.")
        return
    plt.figure(figsize=(10,6))
    plt.plot(df[x_field], df[y_field], marker='o')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel(x_field.capitalize())
    plt.ylabel(y_field.capitalize())
    plt.title(title or f"{y_field.capitalize()} over {x_field.capitalize()}")
    plt.tight_layout()
    plt.show()