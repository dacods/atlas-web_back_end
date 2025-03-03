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
            expect(body).to.equal('Payment methods for cart 5');
            done();
        });
    });

    

    it('should return status code 404 when :id is not a number', (done) => {
        request(`${url}/cart/abc`, (error, response) => {
            expect(response && response.statusCode).to.equal(404);
            done();
        });
    });
});

describe('Available Payments', () => {
    it('should return a JSON object with payment methods', (done) => {
        request(`${url}/available_payments`, { json: true }, (error, response, body) => {
            expect(response && response.statusCode).to.equal(200);
            expect(body).to.deep.equal({
                payment_methods: {
                    credit_cards: true,
                    paypal: false,
            },
        });
        done();
        });
    });
});

describe('Login', () => {
    it('should return Welcome :username when a username is provided', (done) => {
        request.post(
            `${url}/login`,
            {
                json:true,
                body: { userName: 'Name' },
            },
            (error, response, body) => {
                expect(response && response.statusCode).to.equal(200);
                expect(body).to.equal('Welcome Name');
                done();
            }
        );
    });

    it('should return a 400 status when userName is missing', (done) => {
        request.post(
            `${url}/login`,
            {
                json: true,
                body: {},
            },
            (error, response) => {
                expect(response && response.statusCode).to.equal(400);
                expect(response.body).to.equal('Missing userName');
                done();
            }
        );
    });
});