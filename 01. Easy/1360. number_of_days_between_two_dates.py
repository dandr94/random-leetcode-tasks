from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """
        :return: The number of days between the two dates
        """

        # date_1 = datetime.strptime(date1, '%Y-%m-%d').date()
        # date_2 = datetime.strptime(date2, '%Y-%m-%d').date()
        #
        # return abs((date_1 - date_2).days)

        month_and_days = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        def days_since_1971(date: str):
            """
            :return: The number of days since January 1, 1971.
            """
            year, month, day = map(int, date.split('-'))

            # Calculate the number of days for complete years between 1971 and the given year
            for y in range(1971, year):
                if is_leap_year(y):
                    day += 366
                else:
                    day += 365

            # Calculate the number of days for complete months within the given year
            for m in range(1, month):
                if is_leap_year(year) and m == 2:
                    day += 1  # Add one day for February in a leap year
                day += month_and_days[m]

            return day

        def is_leap_year(year: int):
            """
            :return: True if the year is a leap year, False otherwise.
            """

            if year % 4 != 0:
                return False

            if year % 100 == 0 and year % 400 != 0:
                return False

            return True

        # Calculate the absolute difference between the number of days for the two dates
        return abs(days_since_1971(date1) - days_since_1971(date2))


sol = Solution()
print(sol.daysBetweenDates(date1="2019-06-29", date2="2019-06-30"))
print(sol.daysBetweenDates(date1="2020-01-15", date2="2019-12-31"))

# Problem - https://leetcode.com/problems/number-of-days-between-two-dates/
