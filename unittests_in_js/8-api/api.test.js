const request = require('request');
const { expect } = require('chai');
const { response } = require('./api');

describe('Index page', () => {
    const url = 'http://localhost:7865';

    it('should return status code 200', (done) => {
        request(url, (error, response, body) => {
            expect(response && response.statusCode).to.equal(200)
            done();
        });
    });

    it('should return correct response message', (done) => {
        request(url, (error, response, body) => {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
});