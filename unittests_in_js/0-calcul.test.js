const calculateNumber = require('./0-calcul');
const assert = require('assert').strict;

describe('calculateNumber test', function() {
    it('should round the arguments and give the sum', function() {
        assert.strictEqual(calculateNumber(1.1, 2.2), 3);
        assert.strictEqual(calculateNumber(6, 7), 13);
        assert.strictEqual(calculateNumber(-.7, -4.1), -5);
    });
});
