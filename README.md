## Interview task

This project uses Python + Playwright + Behave + Allure for testing AccuWeather.com

<details>
  <summary>
    Installation
  </summary>
  
  ```bash
  pip install -r requirements.txt
  playwright install
  ```
</details>

<details>
  <summary>
    Run behave tests and allure reports
  </summary>

  ```bash
  behave -f allure_behave.formatter:AllureFormatter -o reports/firefox features/
  
  allure serve reports/firefox
  allure generate reports/firefox -o allure-report --clean
  ```
</details>

### Time consumption table

| Date | Activity | Time spent (hr:min) | Comment |
| --- | --- | --- | --- |
| 10.05.25 | Analyzing the interview task | 0:15 | Got familiat with the script and requirements |
| 10.05.25 | Quick review what are the suggested tools | 1 | Reviewed official docs for Playright for Python, BDD, Behave, Allure |
| 10.05.25 | Preparing a local and a Github repository | 0:15 | Created a repo, report.md, and the basic project tree |
| 11.05.25 | Figuring out "how to" everything and first steps | 5:44 | Spent a lot of time to build a project because of plenty amount of information to investigate
| 12.05.25 | Keep looking for the information along coding | 5:16 | Got much closer to the final of the project struggling with pretty obvious and simple stuff because of applying constant changes according to the new findings
| 13.05.25 | Extending the 12.05.25 | 1:38 | Finished 75% of the interview task
| 14.05.25 | Working on the remaining 15% | 4:38 | Spent a lot of time on Chromium and Webkit making them work (had the same problem with the go_back() in-build method using both systems), finished the task
| 15.05.25 | Extending the 14.05.25, reporting and test assignment submission | 1:54 | Prepared all the necessary reports and links
| **Sum** | | **21:10** | |

<table>
  <tr>
    <td align="left">
      <img src="https://wakatime.com/share/@af6dcbd3-bb07-4e16-aadb-02f6c999d678/551008d5-7292-4595-9240-0fa17e19c801.svg" width="500" alt="Wakatime Coding Activities" />
    </td>
    <td align="right">
      <img src="https://wakatime.com/share/@af6dcbd3-bb07-4e16-aadb-02f6c999d678/e0059969-8ff2-4646-81d1-726b126292a5.svg" width="500" alt="Wakatime Languages" />
    </td>
  </tr>
</table>
