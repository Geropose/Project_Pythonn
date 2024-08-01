# import openpyxl

# wb = openpyxl.load_workbook("planilla.xlsx")

# hoja = wb.active

# wb.create_sheet("Hoja 3")
# hoja3 = wb["Hoja 3"]

# hoja3.title = "Nuevo titulo"

# celda = hoja["A1"]
# celda.value = "Nombre completo"

# celda2 = hoja.cell(row=2, column=1)

# for fila in range(1, hoja.max_row + 1):
#     for columna in range(1, hoja.max_column + 1):
#         celda = hoja.cell(row=fila, column=columna)
#         print(celda.value)


# columna = hoja["A"]
# fila = hoja["1"]

# hoja.append([1, 2, 3])

# print(hoja.rows)
# hoja.delete_cols(1, 1)
# hoja.delete_rows(1, 1)

# wb.save("nuevo_excel.xlsx")
