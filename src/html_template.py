#
# HTML Template, is imported to create .html file
#
def html_begin(bewertender_in, zu_bewerten_in) -> str:
    html_file_begin = f"""<div>
                    <table class="content-table" style="border-collapse: collapse;margin: 25px 0;font-size: 0.9em;border-radius: 5px 5px 0 0;overflow: hidden;box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);">
                        <thead>
                            <tr style="background-color: #009879;color: #ffffff;text-align: left;font-weight: bold;">
                                <th style="padding: 12px 15px;"></th>
                                <th style="padding: 12px 15px;"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid #dddddd;">
                                <td style="padding: 12px 15px;"><b>Bewertende Person</b></td>
                                <td style="padding: 12px 15px;">{bewertender_in}</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #dddddd;">
                                <td style="padding: 12px 15px;"><b>Zu Bewertende Person</b></td>
                                <td style="padding: 12px 15px;">{zu_bewerten_in}</td>
                            </tr>
                        </tbody>
                        <thead>
                        <tr style="background-color: #009879;color: #ffffff;text-align: left;font-weight: bold;">
                            <th style="padding: 12px 15px;">Bewertungsschema</th>
                            <th style="padding: 12px 15px;">Punkte</th>
                        </tr>
                        </thead>
                        <tbody>"""
    return html_file_begin

def html_end(checkbox: bool, summe_in, summe_von, kommentar_in, hinweise_in, musterloesung_in) -> str:
    if not checkbox:
            html_file_end = f"""<tr class="active-row" style="border-bottom: 1px solid #dddddd;font-weight: bold;color: #009879;">
                                <td style="padding: 12px 15px;">Summe</td>
                                <td style="padding: 12px 15px;">{summe_in}/{summe_von}</td>
                            </tr>
                            </tbody>
                        </table>
                        <br>
                        <h4>Kommentar</h4>
                        <pre style="white-space:pre-wrap;word-wrap:break-word;">{kommentar_in}</pre>
                        <br>
                        <h4>Hinweise</h4>
                        <pre style="white-space:pre-wrap;word-wrap:break-word;">{hinweise_in}</pre>
                        <br>
                        <h4>Musterlösung</h4>
                        <a href="{musterloesung_in}">{musterloesung_in}</a>
                    </div>
            """
    else:
        html_file_end = f"""<tr class="active-row" style="border-bottom: 1px solid #dddddd;font-weight: bold;color: #009879;">
                            <td style="padding: 12px 15px;">Summe</td>
                            <td style="padding: 12px 15px;">{summe_in}/{summe_von}</td>
                        </tr>
                        </tbody>
                    </table>
                    <p style="font-weight: bold;color: #FF0000;">Compiler Fehler ===> 0 Punkte!</p>
                    <br>
                    <h4>Kommentar</h4>
                    <pre style="white-space:pre-wrap;word-wrap:break-word;">{kommentar_in}</pre>
                    <br>
                    <h4>Hinweise</h4>
                    <pre style="white-space:pre-wrap;word-wrap:break-word;">{hinweise_in}</pre>
                    <br>
                    <h4>Musterlösung</h4>
                    <a href="{musterloesung_in}">{musterloesung_in}</a>
                </div>
        """
    return html_file_end