# Agent log

Add a dated entry each time you work with your AI coding agent, with the newest entry at the bottom. Each entry records what you asked the agent, what it produced, and what you checked or changed. Paste your key prompts in exactly as you typed them. Include at least one time the agent got something wrong, and how you caught it.

Copy this outline for each entry:

```markdown
## YYYY-MM-DD: What you worked on

- **Asked:** "Paste your prompt here."
- **Agent produced:** What it made or changed.
- **Checked or changed:** How you checked it, and what you fixed.
```

## 2026-11-12: Build the ten-question home sales report

- **Asked:** "This is my final project. Read AGENTS.md and docs/data_description_sheet.md first. You have my approval to build this whole step without waiting for a plan review. When you are done, commit the changes and open a pull request into main.\
\
Turn index.html into a long, report-style page that answers ten questions about the home sales data. Each question gets its own section, labeled Q1 to Q10. Each section needs a written answer that states the exact numbers, and a chart that shows the answer, with the key values labeled on the chart or shown in tooltips. Use at least three different chart types across the ten questions. When an answer is one city or a few cities, highlight those cities in an accent color in the chart and keep the rest in a quieter color.\
\
Rules for every number:\
- Valid price: sale_price between 10,000 and 5,000,000, inclusive. Q2 and Q3 say when to use all rows instead.\
- Campus area means the university column (11 values). City means city and state together, for example \"Champaign, IL\" (18 values).\
- Days on market is contract_date minus list_date in days, using only rows that have both dates. A blank date is not zero.\
- Year and month come from sale_date.\
- Use the median unless a question asks for the mean.\
- Round dollars to whole dollars, days, miles and percents to one decimal.\
- Never remove rows because two sales share a street address. listing_id is the key.\
- When two or more cities or campus areas tie, report all of them.\
\
Questions with fixed answers:\
Q1. Which city has the highest median sale price? Show the median sale price of every city.\
Q2. Using all rows (no price rule), which city's mean sale price is furthest above its median, as a percent of the median? Show the mean and median of every city, and explain in one or two sentences what causes the largest gap.\
Q3. Rank the cities by mean sale price twice: once using all rows, and once using valid prices only. Which cities change rank, and by how many positions? Rank 1 is the highest mean.\
Q4. For each campus area, what was the percent change in median sale price from 2024 to 2025? Which campus area had the largest increase, and which campus areas had a decrease?\
Q5. For each campus area, what is the median days on market? Which campus area is the slowest, and which is the fastest?\
Q6. For each campus area, what is the median annual property tax as a percent of the sale price? Use rows with a valid price and a tax_annual_amount greater than 0 and less than the sale price. Which campus area has the highest tax burden, and which has the lowest?\
\
Interactive questions (the chart and the written answer must both update when the visitor changes the controls in that section; compute everything from the data, no fixed numbers; for Q8 and Q10 let the visitor type any amount, not only preset ranges):\
Q7. For a selected number of bedrooms, which city has the lowest median sale price? Show every city's median sale price and number of sales for that bedroom count.\
Q8. For a selected price range, which city has the shortest median days on market? Show every city's median days on market and the number of sales used.\
Q9. For a selected city and year, how many sales were recorded in each month, January to December? Use all rows with a sale date. Identify the month with the most sales.\
Q10. For a selected campus area, maximum budget, and minimum number of bedrooms, what is the median distance to campus (miles_to_campus), and how many sales meet the conditions?\
\
Before you finish, compute the Q1 to Q6 answers a second way (for example with a short script in scripts/) and confirm the page shows the same numbers. Tell me the answers you got."
- **Agent produced:** Replaced the placeholder with a data-driven report and interactive controls, and added `scripts/verify_report.py` for independent Q1–Q6 summaries.
- **Checked or changed:** Compared the page values against the independent pandas results. Browser inspection found that the first Q4 bar chart represented negative changes by their absolute magnitudes and Q10 grouped distances above 9 miles incorrectly; changed Q4 to a diverging chart and retained distance bins through 15+ miles. Verified all ten sections load and the Q7–Q10 answers update after control changes; no browser errors occurred.
