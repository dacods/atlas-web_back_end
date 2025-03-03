const request = require('request');
const { expect } = require('chai');
const { response } = require('./api');
const url = 'http://localhost:7865';

describe('Index page', () => {
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

describe('Cart page', () => {
    it('should return status code 200 when :id is a number', (done) => {
        request(`${url}/cart/5`, (error, response, body) => {
            expect(response && response.statusCode).to.equal(200);
            expect(body).to.equala('Payment methods for cart 5');
        });
    });

    it('should return status code 404 when :id is not a number', (done) => {
        request(`${url}/cart/abc`, (error, response) => {
            expect(response && response.statusCode).to.equal(404);
            done();
        });
    });
});