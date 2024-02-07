# Time Calculator

## Introduction

The `add_time` function is designed to calculate the resulting time after adding a given duration to a specified start time. The function takes three parameters:

- `start`: The starting time in the format 'HH:MM AM/PM'.
- `duration`: The duration to add in the format 'HH:MM'.
- `start_day_of_week` (optional): The starting day of the week as a string.

## How to Use

To use the `add_time` function, follow these steps:

1. **Import the Function:**
   ```python
   from time_calculator import add_time
<!-- Call the Function: -->
<pre>
<code>
result = add_time("11:30 AM", "2:32", "Monday")
</code>
</pre>

<p>In this example, the function will calculate the resulting time after adding 2 hours and 32 minutes to the time 11:30 AM on a Monday.</p>

<!-- Review the Result: -->
<pre>
<code>
print(result)
</code>
</pre>

<p>The function will return the resulting time in the format 'HH:MM AM/PM DayOfWeek'.</p>

<!-- Parameters -->
<h2>Parameters</h2>
<ul>
  <li><code>start</code>: The starting time in the format 'HH:MM AM/PM'.</li>
  <li><code>duration</code>: The duration to add in the format 'HH:MM'.</li>
  <li><code>start_day_of_week</code> (optional): The starting day of the week as a string.</li>
</ul>

<!-- Example -->
<h2>Example</h2>
<pre>
<code>
result = add_time("11:30 AM", "2:32", "Monday")
print(result)
</code>
</pre>

<p>The above example will output the resulting time after adding 2 hours and 32 minutes to the time 11:30 AM on a Monday.</p>

<!-- Notes -->
<h2>Notes</h2>
<ul>
  <li>If the <code>start_day_of_week</code> parameter is not provided, the resulting time will not include the day of the week.</li>
  <li>The function handles both AM and PM times.</li>
  <li>The function accounts for changes in AM/PM when the total sum of hours exceeds 12.</li>
</ul>


