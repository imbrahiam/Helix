

def get_arch():
    return r'..\raw_data\Perfil_EmpresasImpo_2022_WEB.xlsx'


# Aplica estilo al DataFrame
df_final = df_final.style.set_table_styles([
    {
        'selector': 'th',
        'props': [
            ('background-color', '#000000'),
            ('color', '#ffffff'),
            ('text-align', 'center'),
        ]
    },
    {
        'selector': 'td',
        'props': [
            ('background-color', '#ffffff'),
            ('color', '#000000'),
            ('text-align', 'right'),
        ]
    }
])

# Muestra el DataFrame con estilo
print(df_final.to_string())
