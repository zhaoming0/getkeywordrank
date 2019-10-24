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
(async function() {
  let testlink = 'https://members.helium10.com/cerebro';
  await driver.get(testlink);
  await driver.findElement(By.id('loginform-email')).sendKeys('hi920@139.com')
  await driver.findElement(By.id('loginform-password')).sendKeys('GDjhd698VV+')
  await driver.findElement(By.css('#login-form > button')).click()
  await driver.sleep(5000);
  await driver.findElement(By.xpath('//*[@id="wrapper"]/div[3]/div/div/div[2]/div/div/div[1]/span/span[1]/span/ul/li/input'))
  .sendKeys('B07VD4NTX7')
  await driver.findElement(By.xpath('//*[@id="search-form"]/a[1]')).click()
  await driver.sleep(5000);
  // alert
  await driver.findElement(By.xpath('/html/body/div[17]/div[7]')).click()
  await driver.sleep(5000);

  // get table data
  // get tab
  let tables = await driver.findElement(By.xpath('//*[@id="w3"]/table'))
  // get thead
  // await tables.driver.findElement(By.xpath('//*[@id="w3"]/table/thead/tr/th'))
  // get tbody
  let tbody = await driver.findElements(By.xpath('//*[@id="w3"]/table/tbody/tr'))
  let tdnumber = await driver.findElements(By.xpath('//*[@id="w3"]/table/tbody/tr[1]/td'))
  console.log(tdnumber.length)
  console.log(tbody.length)
  let lineText = {}
  for (let i = 1 ; i <= tbody.length; i++) {
    
    let caseResult = []
    for (let j = 1; j <= tdnumber.length; j++) {
      // console.log('i j is :' , i ,' - ', j)
      let xPATH = '//*[@id="w3"]/table/tbody/tr' + '[' + i + ']' + '/td' + '[' + j + ']'
      let xpathText = await driver.findElement(By.xpath(xPATH)).getText();
      caseResult.push(xpathText)
      // console.log(xpathText)
    }
    // console.log('i is :' , i, "\n")
    // console.log(caseResult)
    // console.log(caseResult[0])
    lineText[caseResult[0]] = caseResult
  }
  // for (let i = 1; i <= tbody.length; i++) {
  //   // let aaa = await tbody[i].findElements(By.xpath('./td'))
  //   for (let j = 1; j <= 12; j++) {
  //     // aaa.findElement(By.xpath('./tr'))
  //     // console.log('i is : ',i,' j is : ', j)
  //     // continue;
  //     if ((j = 3 ) && (i = 3)) {
  //       let bbb = '//*[@id="w3"]/table/tbody/tr' + '[' + i + ']' + '/td' + '[' + j + ']'
  //       // let bb = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[',i,']/td[',j,']')).getText()
  //       let ccc = await driver.findElement(By.xpath(bbb)).getText();
  //       console.log(bbb)
  //       console.log(ccc)
  //     //   .then((mesage) => {
  //     //     console.log(message)
  //     //   })
  //     }
  //   }
  //   //*[@id="w3"]/table/tbody/tr[1]/td[7]
  //   //*[@id="w3"]/table/tbody/tr[1]/td[8]
  //   // console.log('111', aaa[0].getText())
  //   // console.log(aaa)
    
  //   // let a1 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[0]')).getText()
  //   let a2 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[1]')).getText()
  //   let a3 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[2]')).getText()
  //   let a4 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[3]')).getText()
  //   let a5 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[4]')).getText()
  //   let a6 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[5]')).getText()
  //   let a7 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[6]')).getText()
  //   let a8 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[7]')).getText()
  //   let a9 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[8]')).getText()
  //   let a10 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[9]')).getText()
  //   let a11 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[10]')).getText()
  //   let a12 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[11]')).getText()
  //   let a13 = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[3]/td[12]')).getText()

  //   console.log( a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13)
  //   // console.log('================================================')
  //   // console.log('title line 2 is :', a3)
  // }

  let b = await driver.findElement(By.xpath('//*[@id="w3"]/table/tbody/tr[6]/td[7]')).getText()
  console.log(b)
  console.log(lineText)
  
  // // await driver.findElement(By.xpath('/html/body/div[20]/div[7]/div/button')).click()
  // let link = 'file:///C:/Users/zhaom/Downloads/Cerebro.html';
  // await driver.get(link)
  // let resultNumber = await driver.findElement(By.xpath('//*[@id="cerebroPjax"]/div[2]/div/div/div/div/div/div[1]/div[1]/div/span')).getText()
  // console.log(resultNumber)
  // let gettitle = await driver.findElement(By.xpath('//*[@id="w3"]/table/thead/tr/th'))
  // console.log(gettitle)
  // console.log(gettitle.length)
  
  })().then(function() {
    console.log('Test completed!');
    driver.sleep(10000)
    driver.quit()
  }).catch(function(err) {
    console.log(err);
    process.exit(1);
  });