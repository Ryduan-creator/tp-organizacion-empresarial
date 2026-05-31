import pandas as pd

ventas = {
    "producto": ["Mouse", "Teclado", "Monitor", "Parlante", "Notebook"],
    "cantidad": [10, 5, 3, 8, 2],
    "precio": [15000, 30000, 200000, 15000, 800000]
}

df = pd.DataFrame(ventas)

df["total"] = df["cantidad"] * df["precio"]

ventas_totales = df["total"].sum()

producto_mas_vendido = (
    df.groupby("producto")["cantidad"]
    .sum()
    .idxmax()
)

print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)
