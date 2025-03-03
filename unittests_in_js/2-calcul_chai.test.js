const calculateNumber = require('./2-calcul_chai');
const assert = require('assert').strict;
const expect = require('chai').expect

describe('calculateNumber test ADD', function() {
    it('should round the arguments and give the sum', function() {
        expect(calculateNumber('SUM', 1.1, 2.2)).to.equal(3);
        expect(calculateNumber('SUM', 6, 7)).to.equal(13);
        expect(calculateNumber('SUM', -.7, -4.1)).to.equal(-5);
    });
});

describe('calculateNumber test SUBTRACT', function() {
    it('should round the arguments and give the difference', function() {
        expect(calculateNumber('SUBTRACT', 2.3, 4.5)).to.equal(-3)
        expect(calculateNumber('SUBTRACT', 5.4, .5)).to.equal(4)
        expect(calculateNumber('SUBTRACT', 7.2, 5.6)).to.equal(1)
    })
});
describe('calculateNumber test DIVIDE', function() {
    it('should round the arguments and give the quotient', function() {
        expect(calculateNumber('DIVIDE', 4.2, 1.6)).to.equal(2)
        expect(calculateNumber('DIVIDE', 10.3, 5.3)).to.equal(2)
        expect(calculateNumber('DIVIDE', 25.3, 5.2)).to.equal(5)
    })
})