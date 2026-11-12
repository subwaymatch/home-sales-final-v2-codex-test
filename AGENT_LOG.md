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

## 2026-11-12: Add dashboard filters, map, comparisons, and themes

- **Asked:** "I merged your pull request into main. Next step: add these required features. Keep the Q1 to Q10 sections working, and do not let the new filters change the Q1 to Q6 answers, which always use the full dataset with the stated rules. You have my approval to go ahead without waiting for a plan review. When you are done, commit the changes and open a pull request into main.\
\
1. Filters and key numbers: filters for campus area or city, year, number of bedrooms, and price range. Show key numbers (median sale price and number of sales) that update automatically when the filters change.\
2. Map filter: an interactive map that shows the city locations. Clicking a location filters the key numbers and related charts to that area. Place each city at the median latitude and longitude of its sales.\
3. Range filter with a slider and number inputs: a range filter for living area with both a draggable range slider and number inputs for the minimum and maximum. The slider and the inputs must stay in sync.\
4. Home feature filter: filter by garage, basement, or fireplace. Treat blanks as unknown, not as \"no\".\
5. Shareable filters: save the current filter settings in the page address, so opening a copied link shows the same view.\
6. Side-by-side comparison: pick two campus areas or cities and compare at least their median sale price and number of sales side by side.\
7. Sortable table: a results table that sorts when a column header is clicked.\
8. Responsive layout: the page, charts, map and controls work on desktop, tablet and phone. On a 375 pixel wide screen nothing should need sideways scrolling.\
9. Light and dark modes: a toggle. Charts, the map, and all controls must stay readable in both.\
10. Data and methods section: state the rules used (the price rule, how days on market is computed, how missing values are handled) and cite the dataset as described in the data description sheet.\
\
Tell me what you built and how you checked it."
- **Agent produced:** Added an interactive filter dashboard with key metrics, median-coordinate city map, living-area dual slider and synced number fields, unknown-aware property features, URL-saved filters, two-area comparisons, sortable results, and light/dark themes. Updated the data/methods notes and README.
- **Checked or changed:** Verified the dashboard at 375px and tablet width with no document horizontal overflow. Checked map selection and copied-link restoration, range input synchronization, feature filters, comparisons, sorting, and theme control colors. Confirmed Q1–Q6 answers remain unchanged while the dashboard filters update. Fixed missing living-area values to remain excluded from the selected numeric range and from area medians.

## 2026-11-12: Add the P1 data-quality insight

- **Asked:** "I merged that pull request. Next, add an Insights section near the end of the page, after Q10 and before Data and methods. You have my approval to go ahead without waiting for a plan review. When you are done, commit the changes and open a pull request into main.\
\
For now, add only P1. Leave a heading for P2 with the text \"Coming soon\"; I will write P2 myself later.\
\
P1. Data quality. Use problem 1 from the data description sheet, \"Days on market needs both dates, a blank is not zero, and the blanks are not random.\" Show, for each city, the share of sales with no list date, and how the city median days on market would change if blanks were wrongly treated as zero days. Include a chart or table that shows the correct and the wrong medians side by side. Then write 150 to 300 words explaining how the site handles the problem, what would have gone wrong otherwise, and what the rule cannot fix (for example, that unlisted sales are more often new construction).\
\
Use exact numbers computed from the data and check them with a script before you finish."
- **Agent produced:** Added an Insights section after Q10 with a complete per-city P1 table, a 259-word data-quality explanation, and the requested P2 “Coming soon” placeholder. Added `scripts/analyze_days_on_market_missingness.py` and documented it in README.
- **Checked or changed:** Ran the pandas script and compared its city counts, shares, correct medians, zero-filled medians, and changes with the rendered table. It reports 35,442 total sales and 28,042 with both dates. Chromium showed 18 city rows, a 259-word explanation, all ten Q sections, P2 text, no JavaScript errors, and no horizontal overflow at 375px.


## 2026-11-12: Design round 1 typography and color

- **Asked:** "I merged that pull request. Design round 1: typography and color. You have my approval to go ahead without waiting for a plan review. When you are done, commit the changes and open a pull request into main with a short description of what changed.\

- Typography: use a free, open-source font from Google Fonts (not the browser default). Pick a pairing that feels like a professional real estate or research report, for example a serif for headings and a clean sans serif for body text and numbers. Make headings, body text, and captions easy to tell apart.\
- Color: define a small palette (neutrals plus one or two accents) as CSS variables, and use it everywhere: charts, the map, buttons, links, and controls. Keep the accent color for highlighted answer cities. Make sure the palette works in both light and dark modes."
- **Agent produced:** Added Newsreader serif display typography with DM Sans for body, data labels, and controls. Consolidated light and dark colors into shared CSS theme variables and applied them to report content, charts, map, controls, links, and buttons. Documented the font and palette choices in README.
- **Checked or changed:** Found and fixed two palette editing errors before browser review: the metrics card referenced an undefined `--navy` token, and two heading rules had redundant serif fallbacks after the font variable. Checked computed font loading, chart/map/control colors, dark theme, and 375px layout in Chromium.


## 2026-11-12: Design round 2 controls and chart finish

- **Asked:** "I merged that pull request. Design round 2: controls and chart finish. You have my approval to go ahead without waiting for a plan review. When you are done, commit the changes and open a pull request into main with a short description of what changed.\

- Controls: style every control (dropdowns, number inputs, slider, toggle, buttons) to match the site instead of browser defaults. Sortable table headers should use proper SVG icons that show which column is sorted and in which direction, not text arrow characters. Add hover states and a visible keyboard focus outline.\
- Chart finish: every chart needs a title and axis labels, formatted numbers (for example $410,000 and 7.6%), no overlapping or cut-off labels, tooltips that match the site's style, and charts that follow the theme in dark mode."
- **Agent produced:** Styled dropdowns, number fields, range sliders, theme and action buttons, and sortable headers with directional SVG icons. Added quantitative and category axis labels, formatted axis ticks, safe label gutters, keyboard-focusable marks, and a shared theme-aware tooltip to all ten charts.
- **Checked or changed:** Chromium confirmed titles and two axis labels across all ten charts, correct currency/percent/day formatting, dark theme chart/tooltip colors, functional sorting and Q7/Q8 updates, and no overflow at 375px. Visual review caught and fixed long campus labels clipping at the left edge. The first sort test also caught the SVG icon intercepting pointer clicks; fixed by disabling pointer events on the decorative icon.


## 2026-11-12: Design round 3 layout and finishing touches

- **Asked:** "I merged that pull request. Design round 3: layout and finishing touches. You have my approval to go ahead without waiting for a plan review. When you are done, commit the changes and open a pull request into main with a short description of what changed.\

- Layout and spacing: use consistent spacing, align elements to a clear grid, keep a comfortable content width, and separate sections clearly. Add a short summary at the top with three key findings and a table of contents that links to each section.\
- Finishing touches: show a loading message while the data loads, a friendly message when filters match no sales, a real page title in the browser tab, and consistent wording and capitalization. Remove any leftover template or placeholder text.\
- Check the page again at 375, 768, and 1280 pixels wide, in both light and dark modes, and fix anything that looks off."
- **Agent produced:** Added a data-driven three-finding summary, a full table of contents with links to the overview, dashboard, questions, Insights, P1/P2, and data/methods, and a descriptive browser title. Standardized loading and empty-filter messages. Tightened layout spacing and made the filtered-results table responsive at mobile/tablet widths and compact at desktop content widths. Reduced map clutter by using selectable median-location dots with the city list below.
- **Checked or changed:** Chromium checked all three requested widths in light and dark themes; page and results table stayed within their content widths, all 17 section links resolved, and there were no browser errors. Verified the loading state, empty filters message, unchanged fixed Q1 answer under dashboard filters, and map city selection. Visual checks caught repeated dark dropdown chevrons, an overpainted dark slider, oversized table sort icons, crowded map labels, and compressed table headings; fixed each before final review. The P2 “Coming soon” placeholder remains because it was explicitly requested for the Insights section in the previous round.
