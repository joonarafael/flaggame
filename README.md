# FLAG QUIZ GAME

![main workflow](https://github.com/joonarafael/flaggame/actions/workflows/main.yml/badge.svg) [![codecov](https://codecov.io/gh/joonarafael/flaggame/graph/badge.svg?token=XCLKOTSKCW)](https://codecov.io/gh/joonarafael/flaggame)

current ver **0.2.8** (_14.4.2024_), **latest release of the software source code** can be found [here](https://github.com/joonarafael/ohte/releases "Flag Game Releases").

This is a **Flag Quiz Game** including all 195 _fully recognized independent states_ listed at [state.gov](https://www.state.gov/independent-states-in-the-world/ "List of independent states at state.gov"), and _Taiwan_, _Kosovo_ & _Western Sahara_. The game has 5 different game modes; _Classic_, _Advanced_, _Time Trial_, _One Life_, and _Free Mode_. See the [Rule Book](./flaggame/src/logs/gamerules.txt "Open Rule Book") for details. The software also records _all user activity_ and _played games_! Player may look previous games and study their **own lifelong statistics**, such as _total playtime_ or _average streak length_!

## DOCUMENTATION

- [User Manual](./documentation/user_manual.md)

- [Software Requirements Specification](./documentation/requirements_specification.md)

- [Software Architecture](./documentation/architecture.md)

- [Changelog](./documentation/changelog.md)

- [Software Testing Document](./documentation/software_testing.md)

## VERSIONS & TECHNICAL DETAILS

**Software has not been tested in a MacOS or Windows environment**. Flag Quiz Game has been built with **Python 3.10**. Software might not run on other versions. You can find the installation manual [here](./documentation/user_manual.md "User Manual").

The software launching and testing etc. are automated with _bash_ scripts. For non-Linux OS users, more technical know-how is required to get the game going.

## SOFTWARE TESTING WITH PYTEST

Run the tests configured with [pytest.ini](./flaggame/pytest.ini "Open the pytest configuration file") (ignoring all graphical user interface modules) by executing:

```bash
./test.sh
```

Navigate to [this folder](./flaggame/src/tests/ "Tests folder") to find all the automated test source files. The tests will take approximately 38 seconds. They are testing e.g. how the points awarding algorithms and statistics calculations work with different round times and scores. See [Software Testing](./documentation/software_testing.md) for a more complete document detailing the software testing process.

## SOFTWARE TEST COVERAGE REPORT

To generate the Coverage report (web browser version) for your local machine, execute:

```bash
./coverage.sh
```

The generated report can be found at `./htmlcov/index.html`.

## PYLINT AUTOMATED CODE REVIEW

To run the automated code review algorithm with parameters defined in [pylintrc](./flaggame/.pylintrc "Open the pylint configuration file"), execute:

```bash
./pylint.sh
```

To read my personal notes about pylint results and other comments regarding software source code quality, check [this document](./documentation/architecture.md#remaining-issues-with-source-code-quality--software-logic "Software Architecture").
