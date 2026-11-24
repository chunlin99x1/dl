import pandas as pd

df = pd.DataFrame({
    'date': ['2020-01-01', '2025-01-02', '2026-01-03', '2026-11-24']
})

df['date'] = pd.to_datetime(df['date'])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
# 获取星期
df["weekday"] = df["date"].dt.weekday
# 星期几
df["weekday_name"] = df["date"].dt.day_name
#获取日期所在季度
df["quarter"] = df["date"].dt.quarter
# 判断日期是不是月底 年底
df["is_end_of_month"] = df["date"].dt.is_month_end

df["is_end_of_year"] = df["date"].dt.is_year_end
print(df)
print(df.dtypes)

## to_period  统计周期
# 创建一个新的 df
df = pd.DataFrame({
    'date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04']
})
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.to_period('Y')
df['month'] = df['date'].dt.to_period('M') # 2020-01
df['day'] = df['date'].dt.to_period('D') #  2020-01-01
# Q1 Q2
df['quarter'] = df['date'].dt.to_period('Q') # 2020Q1





print(df)



