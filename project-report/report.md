# Tetris Score Analysis Server
---
| Zach Levy
| zwlevy@iu.edu
| Indiana University
| hid: sp19-222-97
| github:[:cloud:](https://github.com/cloudmesh-community/sp19-222-97)
| code:[:cloud:](https://github.com/cloudmesh-community/sp19-222-97/tree/master/project-code)
## Abstract
---
The purpose of this project is an inquiry on statistical analysis of various facets of the classic arcade video game, Tetris. Using data recorded from players in an application as well as analyzing the qualities between various factors such as playtime, score, level, and more, the aim is to possibly extract meaningful relationships and evaluate them using standard regression models.
## Introduction
---
Released originally on the Electronika 60 in the USSR on June 6, 1984, Tetris has came from a small programming project from Soviet game designer Alexey Pajitnov to one of the most world-renowned puzzle video games of all time. Although deviations have spawned from the game, the primary rules of Tetris are rather simple. Blocks, arranged into sequences of four called tetrominoes, move vertically from top to bottom. The player can reposition and reorient the blocks, and the goal is to get a set of blocks all on a bottom line, in which the blocks will disappear and add to the score. After many of these occur, the game will speed up, making it harder to arrange blocks correctly. The game is over when the blocks reach to top of the screen.

Tetris is one of the most widely renowned video games of our time. Ported to a wide variety of platforms, it has become a part of popular video game culture and has sold millions of copies. Psychological studies done on people who play the game have lead to the discovery that people who play for prolonged periods of time may see mild remote memories of the images of the tetrominoes moving. Additionally, some studies suggest that Tetris may help reduce mental stress and help individuals cope with post-traumatic stress disorder.
## Design
---
The primary design for this project comes in two stages:

1) The creation of a regression model that most suitable fits the dataset. This should most likely be a linear regression model or a data tree.
2) The creation of a RESTful server that could retrieve the raw data sets, perform analysis, and return the data to a requested user.

The first part of the project required me to program a way to retrieve the transcribed data. By import the Python libraries csv and requests, the program can retrieve this data from a Google Drive downloadable link as TETRIS_DOWNLOAD.csv. This data set can be found [here.](https://drive.google.com/open?id=1ndBqB24w8OnpZmTZTU_Ey2iHdbgxDZgJeuYc66tzhTI)

The analysis of the data was first done with the usage of a linear regression model. For this, I took the features to be year, rounds won, and composite score. The label in question was the resulting ranking of players. The second model used was a data tree classifier. This would help with the previous linear regression model, since we can observe how the Gini coefficients - analytical resultants of data trees that help color the importance of certain variables - are resulted from the usage of a data tree. 

By usage of a data tree node to evaluate linear regression models, we can better understand which relationships between variables are meaningful and which are not.
## Architecture
---

## Dataset
---
The data used within this project was primarily extrapolated from data of the winner results from the Tetris World Championships. Due to the fact that previous years represent data as only image screenshots of spreadsheets, the data had to be manually transcribed into other comma-separated value spreadsheets. Although painstaking, we managed to extract rank, year, rounds played, and composite score from the entries from 2012-2018.
## Results
---
## Conclusion
---
## Sources
---
* http://news.bbc.co.uk/2/hi/health/7813637.stm
* https://science.sciencemag.org/content/290/5490/350
* https://thectwc.com/results/
