import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("college_sleep_and_gpa.csv")
df.columns = df.columns.str.strip()

print("--- VERİ ANALİZİ BAŞLATILDI ---")
print(df[["term_gpa", "avg_sleep_hours"]].describe())


plt.figure(figsize=(10, 6))
plt.scatter(
    df["avg_sleep_hours"], df["term_gpa"], color="teal", alpha=0.5, edgecolor="k"
)

plt.title("Öğrenci Uyku Süresi ile Dönem Not Ortalaması (Term GPA)", fontsize=14)
plt.xlabel("Ortalama Uyku Saati (avg_sleep_hours)", fontsize=12)
plt.ylabel("Dönem GPA (term_gpa)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()


plt.savefig("uyku_ve_term_gpa_analiz.png")
plt.show()