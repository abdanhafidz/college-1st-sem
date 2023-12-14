var express = require('express');
const dbcon = require('../config/db')
const bodyParser = require('body-parser');
var router = express.Router();

router.get('/', function(req, res, next) {
  res.send('respond wit a resource');
});
router.use(bodyParser.urlencoded({ extended: true }));
router.post('/post', (req, res) => {
  const data = req.body;
  res.send("name : "+data.name+", bitches : "+data.bitches);
  // dbcon.mysqli_query("INSERT INTO users SET nama = 'Abdan', username='abdanhafidz', password='123' ")
})
module.exports = router;

