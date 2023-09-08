# Python Demos

> 记录一些常用的Python小工具例子。

- [Python Demos](#python-demos)
  - [Email Bot](#email-bot)
  - [CLI](#cli)

## Email Bot

有时候我们会希望将一些重要信息通过Email的方式告知某些人，比如：报表的汇总信息、账号的登录提醒等等。此时，了解如何使用Python发送Email就十分重要了。

使用Python发送Email，首先要确保邮箱账号支持SMTP服务，并开启该服务。以企业微信邮箱为例，可在登录企业微信管理端【协作->设置->第三方客户端】开启/修改POP/SMTP服务或者IMAP/SMTP服务范围，更详细的操作可以参考腾讯官方教程[如何开启腾讯企业邮箱的POP/SMTP/IMAP服务？](https://open.work.weixin.qq.com/help2/pc/19886?person_id=1)。

## CLI

之前我也尝试使用Golang以及Cobra框架去实现一个CLI工具，但考虑到Python在数据处理方面的强大功能。当需要实现一款主要用于处理数据的CLI工具时，使用Python就成为不可避免的事情了。

和Cobra框架相比，Python内置的Argparse包相对较简单，易于上手和使用，具体可以参考我的CLI Demo。
