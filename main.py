import matplotlib.pyplot as plt
import numpy as np
import os

# ==========================================
# CONFIGURAÇÃO DE ESTILO E AMBIENTE
# ==========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_NAME = "Impact_Dashboard.png"

# Configuração de estilo para visualização profissional
plt.rcParams['font.sans-serif'] = 'Arial'  # Fonte padrão compatível
plt.rcParams['axes.facecolor'] = 'none'
plt.rcParams['axes.labelcolor'] = '#444444'

def format_spines(ax):
    """Remove bordas desnecessárias para um look moderno."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#DDDDDD')
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(colors='#666666', labelsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.3)

# ==========================================
# BLOCO DE DADOS (KPIs do Projeto)
# ==========================================
anos = ['Year 1', 'Year 2', 'Year 3']

# A1: Capacitação
docentes_formadores = [20, 20, 78]
docentes_formados = [0, 25, 78]

# A2: Impacto Académico
total_uc_impactadas = [4, 20, 32]
sensibilizacao_eds_perc = [0, 49, 72]
mestrados_dissertacao_ods_perc = [0, 46, 67]

# A3: Recursos Pedagógicos
modulos_formacao_criados = [0, 3, 0]
conteudos_digitais = [3, 0, 2]

# A4: Envolvimento Comunitário
metrics = [
    [3, 9, 8],  # Palestras
    [2, 2, 9],  # Campanhas
    [2, 3, 9],  # Eventos
    [3, 4, 3]   # Iniciativas
]
labels = ['Lectures', 'Campaigns', 'Events', 'Student Initiatives']
colors = ['#C0392B', '#E67E22', '#2980B9', '#16A085']

# ==========================================
# GERAÇÃO DO DASHBOARD
# ==========================================
fig, axs = plt.subplots(2, 2, figsize=(16, 12), facecolor='#FFFFFF')
fig.suptitle('Project Impact Dashboard: Education for Sustainable Development', 
             fontsize=24, fontweight='bold', color='#2C3E50', y=0.98)

# --- 1: Teacher Training (A1) ---
x = np.arange(len(anos))
width = 0.35
axs[0, 0].bar(x - width/2, docentes_formadores, width, label='Trainers', color='#1B4F72', alpha=0.9)
axs[0, 0].bar(x + width/2, docentes_formados, width, label='Trained Faculty', color='#3498DB', alpha=0.9)
axs[0, 0].set_title('Faculty Capacity Building', fontsize=14, fontweight='bold', pad=15)
axs[0, 0].set_xticks(x)
axs[0, 0].set_xticklabels(anos)
axs[0, 0].legend(frameon=False)
format_spines(axs[0, 0])

# --- 2: Academic Impact (A2) ---
ax2_twin = axs[0, 1].twinx()
axs[0, 1].fill_between(anos, total_uc_impactadas, color='#27AE60', alpha=0.1)
l1, = axs[0, 1].plot(anos, total_uc_impactadas, color='#27AE60', marker='o', linewidth=4, label='Courses Adapted')
l2, = ax2_twin.plot(anos, sensibilizacao_eds_perc, color='#D35400', marker='s', linestyle='--', label='% Student Awareness')
l3, = ax2_twin.plot(anos, mestrados_dissertacao_ods_perc, color='#F39C12', marker='^', linestyle=':', label='% ODS Dissertations')
axs[0, 1].set_title('Curriculum Integration', fontsize=14, fontweight='bold', pad=15)
axs[0, 1].legend(handles=[l1, l2, l3], frameon=False, loc='upper left')
format_spines(axs[0, 1])

# --- 3: Resource Production (A3) ---
axs[1, 0].bar(anos, modulos_formacao_criados, color='#8E44AD', alpha=0.3, label='Training Modules')
axs[1, 0].plot(anos, conteudos_digitais, color='#8E44AD', marker='D', linewidth=3, label='Digital Content')
axs[1, 0].set_title('Educational Resources', fontsize=14, fontweight='bold', pad=15)
axs[1, 0].legend(frameon=False)
format_spines(axs[1, 0])

# --- 4: Community Engagement (A4) ---
for i in range(len(metrics)):
    axs[1, 1].plot(anos, metrics[i], color=colors[i], marker='o', linewidth=2.5, label=labels[i])
axs[1, 1].set_title('Non-Formal Education Outreach', fontsize=14, fontweight='bold', pad=15)
axs[1, 1].legend(frameon=False, ncol=2)
format_spines(axs[1, 1])

# Finalização
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
save_path = os.path.join(BASE_DIR, OUTPUT_NAME)
plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"Dashboard generated successfully: {save_path}")
