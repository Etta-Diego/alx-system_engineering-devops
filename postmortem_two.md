---


---

<div>  <h2>Postmortem: Nginx Not Listening on Port 80.</h2><h2>  </h2></div>
<div>
<img src="https://i.imgur.com/VtLKeHd.jpg" alt="a man blocked his ears and a hand with speakers">
</div>
<p>Incident Summary:</p>
<div>
  <img src="https://i.imgur.com/cO4Lxv9.png" alt="meme of Mr Grub describing the incident">
</div>
<p>Between the hours of 6:00 AM on August 10, 2024, and 10:00 AM on August 10, 2024, our web application experienced an outage. due to Nginx not listening on port 80 on a production server running Ubuntu. This incident was triggered by a misconfiguration change applied at 5:45 AM on August 10, 2024, during a routine server update. The configuration file for Nginx was inadvertently altered, preventing the service from binding to port 80. The issue was detected by our monitoring system, which alerted the on-call engineer. This high-severity incident affected 100% of incoming traffic to our application for approximately 4 hours, leading to a significant impact on user access. During this period, 150 support tickets were submitted, and the issue was widely discussed on social media.</p>
<p>Leadup</p>
<p><img src="https://i.imgur.com/zWw0qKy.jpg" alt="enter image description here"></p>
<p>At 5:45 AM on August 10, 2024, approximately 15 minutes before the customer impact, a routine server update was performed on the production environment. This update included changes to the Nginx configuration file to improve performance. However, an error in the configuration syntax prevented Nginx from successfully binding to port 80, which is essential for handling HTTP requests. This misconfiguration went unnoticed due to the lack of syntax validation before deployment.</p>
<p>Fault</p>
<p><img src="https://i.imgur.com/kxiERIa.png" alt="enter image description here"></p>
<p>The change implemented involved altering the Nginx configuration to adjust the default server block settings. However, a syntax error was introduced in the configuration file, specifically within the <code>listen</code> directive, which caused Nginx to fail in binding to port 80. Consequently, all HTTP requests to the server were rejected, resulting in a complete service outage. This misconfiguration led to 100% of incoming HTTP requests being rejected for the duration of the incident.</p>
<p>Impact</p>
<p><img src="https://i.imgur.com/YRxwUTH.jpg" alt="enter image description here"></p>
<p>For 4 hours between 6:00 AM and 10:00 AM on August 10, 2024, our users experienced a complete outage of our web application due to Nginx not listening on port 80. This incident affected all active users of our web service, with an estimated 10,000 users unable to access the platform. During this period, 150 support tickets were submitted, and the incident was mentioned in over 300 social media posts, highlighting user frustration and concern.</p>
<p>Detection</p>
<p><img src="https://i.imgur.com/AObIG8j.png" alt="enter image description here"></p>
<p>The incident was detected at 6:05 AM by our monitoring system, which triggered an alert due to the sudden drop in incoming traffic to the server. The on-call engineer was paged immediately, but there was a delay of 15 minutes in response time due to the engineer being unfamiliar with the specific configuration error. To improve time-to-detection, we plan to implement more rigorous configuration checks and automated syntax validation in our CI/CD pipeline, which would have cut the detection time by half.</p>
<p>Response</p>
<p><img src="https://i.imgur.com/55iZgCJ.png" alt="enter image description here"></p>
<p>The on-call engineer responded to the page at 6:20 AM and began investigating the issue. However, due to the complexity of the configuration error, a second escalation was required. The escalated engineer, with specific knowledge of Nginx, was alerted at 6:35 AM and began working on the issue. The root cause was identified at 9:00 AM, and a corrected configuration file was deployed at 9:45 AM.</p>
<p>Recovery</p>
<p><img src="https://i.imgur.com/8hzbUHz.png" alt="enter image description here"></p>
<p>The service was restored by reverting the Nginx configuration file to the last known working state and performing a syntax check before restarting the service. The service was fully operational again by 10:00 AM. To improve the time to mitigation, automated tests for configuration changes will be added to the deployment process, which could have potentially cut the recovery time by half.</p>
<p>Timeline</p>
<p><img src="https://i.imgur.com/9iwX2md.png" alt="enter image description here"></p>
<p>5:45 AM UTC<br>
Routine server update applied; Nginx configuration file altered.</p>
<p>6:00 AM UTC<br>
Nginx fails to bind to port 80; service outage begins.</p>
<p>6:05 AM UTC 	<br>
Monitoring system detects the issue; on-call engineer is paged.</p>
<p>6:20 AM UTC<br>
On-call engineer responds; begins investigation.</p>
<p>6:35 AM UTC<br>
Escalation to a second engineer with Nginx expertise.</p>
<p>9:00 AM UTC<br>
Root cause identified.</p>
<p>9:45 AM UTC<br>
Corrected configuration deployed<br>
.<br>
10:00 AM UTC<br>
Nginx successfully binds to port 80; service restored.</p>
<p>Root Cause Identification: The Five Whys</p>
<p><img src="https://i.imgur.com/WSpnPuG.jpg" alt="enter image description here"></p>
<p>Why did the application have an outage?<br>
Because Nginx was not listening on port 80</p>
<p>Why was Nginx not listening on port 80?**<br>
Because there was a syntax error in the Nginx configuration file.</p>
<p>Why was there a syntax error in the configuration file?<br>
Because a misconfiguration was introduced during a routine update.</p>
<p>Why was the misconfiguration not detected before deployment?<br>
Because there were no automated syntax checks in place during the deployment process.</p>
<p>Why were there no syntax checks in the deployment process?<br>
Because the importance of syntax validation was underestimated in the CI/CD pipeline.</p>
<p>Root Cause</p>
<p><img src="https://i.imgur.com/TYlHLPg.jpg" alt="enter image description here"></p>
<p>The root cause of the incident was a syntax error in the Nginx configuration file, combined with the lack of automated syntax validation in the deployment process.</p>
<p>Backlog Check</p>
<p><img src="https://i.imgur.com/MwN44iZ.png" alt="enter image description here"></p>
<p>There were no specific items in the engineering backlog that could have prevented this incident. However, there were ongoing tasks related to improving the deployment process, including the addition of automated tests, which had not yet been prioritized.</p>
<p>Recurrence<br>
<img src="https://i.imgur.com/xdZZr3c.jpg" alt="enter image description here"></p>
<p>A similar incident occurred two months prior, where a configuration error led to a partial outage. The mitigation at the time involved manual checks, which were not effective in preventing this incident. The lack of automated validation has been a recurring issue.</p>
<p>Lessons Learnt</p>
<p><img src="https://i.imgur.com/KWy29v6.png" alt="enter image description here"></p>
<p>What went well:<br>
The monitoring system effectively detected the drop in traffic and triggered an alert.<br>
What could have been improved:<br>
The response time was delayed due to the lack of familiarity with the configuration issue.<br>
Opportunities for improvement:<br>
Automated syntax validation should be implemented to catch configuration errors before deployment.</p>
<p>Corrective Actions</p>
<p><img src="https://i.imgur.com/MuyxSLu.jpg" alt="enter image description here"></p>
<p>Responsible: DevOps team<br>
Action: Implement automated syntax validation for Nginx configurations in the CI/CD pipeline.<br>
Deadline: September 1, 2024<br>
Tracking: Jira Ticket #NGX-7890</p>

