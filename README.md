# FLAG QUIZ GAME

current ver **0.2.8** (_14.4.2024_), **latest release of the software source code** can be found [here](https://github.com/joonarafael/ohte/releases "Flag Game Releases").

This is a **Flag Quiz Game** including all 195 _fully recognized independent states_ listed at [state.gov](https://www.state.gov/independent-states-in-the-world/ "List of independent states at state.gov"), and _Taiwan_, _Kosovo_ & _Western Sahara_. The game has 5 different game modes; _Classic_, _Advanced_, _Time Trial_, _One Life_, and _Free Mode_. See the [rulebook](./flaggame/src/logs/gamerules.txt "Open Rule Book") for details. The software also records _all user activity_ and _played games_! Player may look previous games and study their **own lifelong statistics**, such as _total playtime_ or _average streak length_!

## DOCUMENTATION

- [User Manual](./documentation/user_manual.md)

- [Software Requirements Specification](./documentation/requirements_specification.md)

- [Software Architecture](./documentation/architecture.md)

- [Changelog](./documentation/changelog.md)

- [Software Testing Document](./documentation/software_testing.md)

## VERSIONS

**Software has not been tested in a MacOS or Windows environment**. Flag Quiz Game has been built with **Python 3.10**. Software might not run on other versions. You can find the installation manual [here](./documentation/user_manual.md "User Manual")

## SOFTWARE TESTING WITH PYTEST

Run the tests configured with [pytest.ini](./flaggame/pytest.ini) (ignoring all graphical user interface modules) by executing:

```bash
poetry run invoke test
```

Navigate to [this folder](./flaggame/src/tests/) to find all the automated test source files. The tests will take approximately 38 seconds. They are testing e.g. how the points awarding algorithms and statistics calculations work with different round times and scores. See [Software Testing](./documentation/software_testing.md) for a more complete document detailing the software testing process.

## SOFTWARE TEST COVERAGE REPORT

To generate the Coverage report (web browser version) for your local machine, execute:

```bash
poetry run invoke coverage-report
```

The generated report can be found at `./flaggame/htmlcov/index.html`.

Please note: if running the Coverage tool on a Horizon virtual desktop, execution might halt due to a SQLite error: `database is locked`. This is a direct consequence of the insufficient speed of the virtual disk (see [this page](https://ohjelmistotekniikka-hy.github.io/python/toteutus#sqlite-tietokanta-lukkiutuminen-virtuaality%C3%B6asemalla) for details). To fix this issue, the whole repository needs to be cloned in to the `/tmp` system directory for proper execution. Move to this system directory and follow the instructions from the [beginning](./README.md#installation-guide) again.

```bash
cd /tmp
```

## PYLINT AUTOMATED CODE REVIEW

To run the automated code review algorithm with parameters defined in [pylintrc](./flaggame/.pylintrc), execute:

```bash
poetry run invoke lint
```

To read my personal notes about pylint results and other comments regarding software source code quality, see [Software Architecture](./documentation/architecture.md#remaining-issues-with-source-code-quality--software-logic).
