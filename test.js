const webdriver = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

const By = webdriver.By;
const Key = webdriver.Key;
const options = new chrome.Options();
// options.addArguments('no-sandbox');
const builder = new webdriver.Builder();
builder.forBrowser('chrome');
builder.setChromeOptions(options);
const driver = builder.build();
const csv = require('./node_modules/fast-csv');
const fs = require('fs');
const os = require('os');

var lineText = {};

(async function() {
  let testlink = 'https://members.helium10.com/cerebro';
  await driver.get(testlink);
  await driver.findElement(By.id('loginform-email')).sendKeys('hi920@139.com')
  await driver.findElement(By.id('loginform-password')).sendKeys('GDjhd698VV+')
  await driver.findElement(By.css('#login-form > button')).click()
  await driver.sleep(5000);
  await driver.findElement(By.xpath('//*[@id="wrapper"]/div[3]/div/div/div[2]/div/div/div[1]/span/span[1]/span/ul/li/input'))
  .sendKeys('B07WQ284PG')
  await driver.findElement(By.xpath('//*[@id="search-form"]/a[1]')).click()
  await driver.sleep(5000);
  // alert
  await driver.findElement(By.xpath('/html/body/div[17]/div[7]')).click()
  await driver.sleep(5000);

  // get tab
  let tables = await driver.findElement(By.xpath('//*[@id="w3"]/table'))

  // get totall number key word
  let totalKeyWord = await driver.findElement(By.xpath('//*[@id="cerebroPjax"]/div[2]/div/div/div/div/div/div[1]/div[1]/div/span')).getText()
  totalKeyWord = Number(totalKeyWord.match(/\d/g).join(''))
  
  // await tables.driver.findElement(By.xpath('//*[@id="w3"]/table/thead/tr/th'))
  let tbody = await driver.findElements(By.xpath('//*[@id="w3"]/table/tbody/tr')) //50 
  let tdnumber = await driver.findElements(By.xpath('//*[@id="w3"]/table/tbody/tr[1]/td')) //12
  let totalPages = parseInt(totalKeyWord/tbody.length)
  
  for (let num = 1; num <= totalPages + 1; num++) {
    tbody = await driver.findElements(By.xpath('//*[@id="w3"]/table/tbody/tr'))
    // console.log('tbody is :', tbody.length)
    for (let i = 1 ; i <= tbody.length; i++) {
      let caseResult = []
      for (let j = 1; j <= tdnumber.length; j++) {
        let xPATH = '//*[@id="w3"]/table/tbody/tr' + '[' + i + ']' + '/td' + '[' + j + ']'
        let xpathText = await driver.findElement(By.xpath(xPATH)).getText();
        caseResult.push(xpathText)
      }
      lineText[caseResult[0]] = caseResult
    }
    if (num <= totalPages) {
      await driver.findElement(By.xpath('//*[@id="w3"]/ul/li[10]/a')).click();
      // await driver.findElement(By.xpath('//*[@id="w3"]/ul/li[12]/a')).click();
      driver.sleep(5000)
    }
  }
  
  })().then(function() {
    console.log('Test completed!');
    driver.sleep(10000)
    // driver.quit()
    console.log(lineText)
  }).catch(function(err) {
    console.log(err);
    process.exit(1);
  });