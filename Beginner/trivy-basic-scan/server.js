const express = require('express');
const _ = require('lodash');
const app = express();

// Example route that uses lodash merge (demonstrating vulnerable code path)
app.get('/', (req, res) => {
    let safe = { user: 'guest' };
    // this merge could be exploited if lodash prototype-pollution vulnerability is present
    let merged = _.merge(safe, req.query);
    res.send(`Hello, ${merged.user}`);
});

app.listen(3000, () => {
    console.log('Demo app listening on http://localhost:3000');
});
