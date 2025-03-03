const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');
const calculateNumber = require('./0-calcul');

describe('sendPaymentRequestToApi', function() {
    it('should call calculatNumber with "SUM", totalAmount, totalShipping', function() {
        const spy = sinon.spy(Utils, 'calculateNumber');
        
        sendPaymentRequestToApi(100, 20);

        expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
        spy.restore();
    })
})