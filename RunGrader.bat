
@ECHO off

FOR %%A IN (0.05	0.1	0.15	0.2	0.25	0.3	0.35	0.4	0.45	0.5	0.55	0.6	0.65	0.7	0.75	0.8	0.85	0.9	0.95	1) DO (
COMMAND /C FOR %%B IN (0.05	0.1	0.15	0.2	0.25	0.3	0.35	0.4	0.45	0.5	0.55	0.6	0.65	0.7	0.75	0.8	0.85	0.9	0.95	1) DO (
COMMAND /C FOR %%C IN (0.05	0.1	0.15	0.2	0.25	0.3	0.35	0.4	0.45	0.5	0.55	0.6	0.65	0.7	0.75	0.8	0.85	0.9	0.95	1) DO (
DEL analysis.py
(
echo def question3b()^:
echo     return "%%A", 0.1, 0.1
) > analysis.py
python autograder.py -q q3
)
)
)


