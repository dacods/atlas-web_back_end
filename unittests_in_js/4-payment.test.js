const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi stub', function() {
    it('should stub utils.calculatNumber to always return 10', function() {
        const spy = sinon.spy(console, 'log');
        const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
        
        sendPaymentRequestToApi(100, 20);

        expect(spy.calledOnceWithExactly('The total is: 10')).to.be.true;
        expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

        spy.restore();
        stub.restore();
    })
})