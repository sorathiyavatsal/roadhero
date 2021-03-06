from decouple import config
from django.core.mail import EmailMultiAlternatives


def sendEmailsWithoutBroker(subject, message, to_email, message_html, requested_by):
    from_mail = config('DEFAULT_FROM_EMAIL')
    regards = "Dear "

    # function to send mail using ses
    msg = EmailMultiAlternatives(
        str(config('DEFAULT_SUBJECT_PREFIX')) + f' : {subject}',
        standard_email_template(message, message_html, requested_by, regards),
        from_mail,
        list(set(to_email))
    )

    msg.attach_alternative(standard_email_template(message, message_html, requested_by, regards), "text/html")
    msg.send()
    return


def standard_email_template(message, message_html, requested_by, regards):
    html = """
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <meta name="viewport" content="width=device-width"/>

            <style type="text/css">


                * { margin: 0; padding: 0; font-size: 100%; font-family: 'Avenir Next', "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif; line-height: 1.65; }

                img { max-width: 100%; margin: 0 auto; display: block; }

                body, .body-wrap { width: 100% !important; height: 100%; background: #f8f8f8; }

                a { color: #71bc37; text-decoration: none; }

                a:hover { text-decoration: underline; }

                .text-center { text-align: center; }

                .text-right { text-align: right; }

                .text-left { text-align: left; }

                .button { display: inline-block; color: white; background: #71bc37; border: solid #71bc37; border-width: 10px 20px 8px; font-weight: bold; border-radius: 4px; }

                .button:hover { text-decoration: none; }

                h1, h2, h3, h4, h5, h6 { margin-bottom: 15px; line-height: 1.25; }

                h1 { font-size: 24px; }

                h2 { font-size: 20px; }

                h3 { font-size: 16px; }

                h4 { font-size: 12px; }

                h5 { font-size: 10px; }

                p, ul, ol, th, td { font-size: 14px; font-weight: normal; margin-bottom: 10px; }

                .details-table th { border:1px solid #bababa; padding: 10px }

                .details-table td { border:1px solid #bababa; padding: 10px }

                .container { display: block !important; clear: both !important; margin: 0 auto !important; max-width: 1100px !important; }

                .container table { width: 100% !important; border-collapse: collapse; }

                .container .masthead { padding: 5px 0; background: #71bc37; color: white; }

                .container .masthead h2 { margin: 0 auto !important; max-width: 90%; text-transform: uppercase; }

                .container .content { background: white; padding: 30px 35px; }

                .container .content.footer { background: none; }

                .container .content.footer p { margin-bottom: 0; color: #888; text-align: center; font-size: 14px; }

                .container .content.footer a { color: #888; text-decoration: none; font-weight: bold; }

                .container .content.footer a:hover { text-decoration: underline; }
                a.button {
                    -webkit-appearance: button;
                    -moz-appearance: button;
                    appearance: button;

                    background-color: #008CBA; /* Green */
                    border: none;
                    padding: 7px 7px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 17px;
                    border-radius: 3px;
                    color:#fff;
}


            </style>
        </head>
        <body>
        <table class="body-wrap">
            <tr>
                <td class="container">

                    <!-- Message start -->
                    <table>
                        <tr>
                            <td align="center" class="masthead">

                                <h1>RoadHeroes</h1>

                            </td>
                        </tr>
                        <tr>
                            <td class="content">

                                <h3> """ + regards + requested_by + """,</h3>

                                <p>""" + message + """</p>

                                <p>""" + message_html + """</p>


                                <p></p>
                                <br/>
                                <br/>
                                <p>For critical issues you will generally receive a response within 2 business hours. All other issues will be prioritized within 24 hours.</p>


                            </td>
                        </tr>
                    </table>

                </td>
            </tr>
            <tr>
                <td class="container">

                    <!-- Message start -->
                    <table>
                        <tr>
                            <td class="content footer" align="center">
                                <p>Copyright?? 2021 RoadHeroes, Inc.</p>
                            </td>
                        </tr>
                    </table>

                </td>
            </tr>
        </table>
        </body>
        </html>
        """
    return html
