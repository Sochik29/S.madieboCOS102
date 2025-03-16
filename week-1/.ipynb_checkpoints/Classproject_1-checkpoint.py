{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa685cd0-8a37-4818-8dd0-9878c329f640",
   "metadata": {},
   "outputs": [],
   "source": [
    "def simple_interest(P, R, T):\n",
    "    return P * (1 + (R / 100) * T)\n",
    "\n",
    "def compound_interest(P, R, n, t):\n",
    "    return P * (1 + R / (n * 100))**(n * t)\n",
    "\n",
    "def annuity_plan(PMT, R, n, t):\n",
    "    R /= 100  # Convert rate to decimal\n",
    "    return PMT * ((1 + R/n)**(n*t) - 1) / (R/n)\n",
    "\n",
    "# User Input\n",
    "choice = int(input(\"Choose Calculation:\\n1. Simple Interest\\n2. Compound Interest\\n3. Annuity Plan\\nEnter choice: \"))\n",
    "\n",
    "if choice == 1:\n",
    "    P, R, T = map(float, input(\"Enter Principal, Rate (%), Time (years): \").split())\n",
    "    print(f\"Amount: {simple_interest(P, R, T):.2f}\")\n",
    "\n",
    "elif choice == 2:\n",
    "    P, R, n, t = map(float, input(\"Enter Principal, Rate (%), Compounds per Year, Time (years): \").split())\n",
    "    print(f\"Amount: {compound_interest(P, R, int(n), t):.2f}\")\n",
    "\n",
    "elif choice == 3:\n",
    "    PMT, R, n, t = map(float, input(\"Enter Payment, Rate (%), Periods per Year, Time (years): \").split())\n",
    "    print(f\"Annuity Value: {annuity_plan(PMT, R, int(n), t):.2f}\")\n",
    "\n",
    "else:\n",
    "    print(\"Invalid choice!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "888003b7-3133-4fd6-835c-f90f1d036c5e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
