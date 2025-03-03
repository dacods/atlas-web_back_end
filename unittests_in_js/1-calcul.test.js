const calculateNumber = require('./1-calcul');
const assert = require('assert').strict;

describe('calculateNumber test ADD', function() {
    it('should round the arguments and give the sum', function() {
        assert.strictEqual(calculateNumber('SUM', 1.1, 2.2), 3);
        assert.strictEqual(calculateNumber('SUM', 6, 7), 13);
        assert.strictEqual(calculateNumber('SUM', -.7, -4.1), -5);
    });
});

describe('calculateNumber test SUBTRACT', function() {
    it('should round the arguments and give the difference', function() {
        assert.strictEqual(calculateNumber('SUBTRACT', 2.3, 4.5,), -3)
        assert.strictEqual(calculateNumber('SUBTRACT', 5.4, .5,), 4)
        assert.strictEqual(calculateNumber('SUBTRACT', 7.2, 5.6,), 1)
    })
});
describe('calculateNumber test DIVIDE', function() {
    it('should round the arguments and give the quotient', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 4.2, 1.6), 2)
        assert.strictEqual(calculateNumber('DIVIDE', 10.3, 0), 'Error')
        assert.strictEqual(calculateNumber('DIVIDE', 25.3, 5.2), 5)
    });
})