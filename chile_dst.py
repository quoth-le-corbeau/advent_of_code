import pandas as pd

day_before_spring_back_chile = pd.Timestamp("2025-09-06 00:00", tz="Chile/Continental")
one_day_after_spring_back_chile = day_before_spring_back_chile + pd.Timedelta(days=1)
one_day_after_one_day_after_spring_back_chile = (
    one_day_after_spring_back_chile + pd.Timedelta(days=1)
)
print(f"{day_before_spring_back_chile=}")
print(f"{one_day_after_spring_back_chile=}")
print(f"{one_day_after_one_day_after_spring_back_chile=}")
print(f"{day_before_spring_back_chile.dst().seconds=}")
print(f"{one_day_after_spring_back_chile.dst().seconds=}")
