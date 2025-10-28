# 🧬 Sex-Linked Inheritance: Calico (Tortoiseshell) Cat Simulator

This interactive Streamlit app simulates **X-chromosome inactivation** in female cats (commonly known as *tortoiseshell* or *calico* cats).  
It visually represents the random mosaic pattern of fur coloration that arises when one of the two X chromosomes is inactivated in each cell.

---

## 🎯 Purpose

In cats, the gene for fur color (orange or black) is located on the **X chromosome**:

- `XB` → black pigment  
- `Xb` → orange pigment  

Only **females (XX)** can be heterozygous (`XB Xb`), expressing both pigments due to random X inactivation.  
This produces the characteristic **bicolor tortoiseshell pattern**.  
*(Note: the white color in tricolor cats results from other genes and is not part of this simulation.)*

This project is designed for **educational purposes** — ideal for teaching basic principles of **sex-linked inheritance** and **mosaicism** in genetics courses.

---

## ⚙️ How It Works

1. Click **"Perform Cross"** to simulate a genetic cross between a black male (`BB`) and an orange female (`bb`).  
2. A random pattern of yellow and black squares appears, symbolizing the random inactivation of one X chromosome in each cell.  
3. Each time you press the button, a **new random pattern** is generated.

---

## 🧩 Technologies Used

- **Python 3.10+**  
- **Streamlit** for the interactive web interface  
- **Matplotlib** and **NumPy** for grid visualization  

---

## 🚀 Installation and Run

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/cat-genetics-simulator.git
cd cat-genetics-simulator
pip install -r requirements.txt
