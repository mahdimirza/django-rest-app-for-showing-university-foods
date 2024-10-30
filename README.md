<!DOCTYPE html>
<html lang="en">


<h1>Django REST App for Showing University Foods</h1>

<h2>Overview</h2>
<p>This program receives all the meals of the week via a JSON and returns the meals for today or tomorrow based on the request time.</p>

<h2>Available Endpoints</h2>
<ul>
    <li><strong><code>all-foods/</code></strong>: Displays all of the foods available for the current week.</li>
    <li><strong><code>dining/</code></strong>: 
        <ul>
            <li>If lunch time is over, this endpoint shows today's dinner and tomorrow's lunch.</li>
            <li>Otherwise, it shows both today's lunch and dinner.</li>
        </ul>
    </li>
    <li><strong><code>insert-foods/</code></strong>: Allows users to create new food entries.</li>
    <li><strong><code>just-lunch/</code></strong>: Displays only the lunches available for native students.</li>
</ul>

</body>
</html>
