# Postmortem: Optimum.com Email Service Outage

## Issue Summary
- **Duration**: The outage lasted from May 3, 2024, 09:00 AM to May 3, 2024, 12:30 PM (3.5 hours).
- **Impact**: The email service on optimum.com was completely inaccessible. Approximately 65% of users experienced an inability to sign in to their accounts. This affected both personal and business communications, leading to significant disruptions.
- **Root Cause**: The root cause was identified as a configuration error in the load balancer, which incorrectly directed traffic away from the email service servers.

## Timeline
- **09:00 AM** - Outage began; users started experiencing sign-in issues.
- **09:15 AM** - The issue was first detected through automated monitoring alerts indicating server unresponsiveness.
- **09:30 AM** - Initial investigation by the IT support team focused on server health and network connectivity.
- **09:45 AM** - User complaints started to escalate, prompting broader internal communication about the issue.
- **10:00 AM** - Misleading leads pointed towards a possible DDoS attack; cybersecurity team engaged.
- **10:30 AM** - Further analysis ruled out DDoS, refocusing on internal network configurations.
- **11:00 AM** - Incident escalated to the network operations team; load balancer configurations identified as a potential cause.
- **11:45 AM** - Confirmed configuration error in the load balancer.
- **12:00 PM** - Corrective actions taken to reconfigure the load balancer.
- **12:30 PM** - Service restored; monitoring continued to ensure stability.

## Root Cause and Resolution
- **Cause**: A routine update to the load balancer configuration was incorrectly applied, which led to traffic being misrouted and thus preventing users from accessing the email service.
- **Resolution**: The issue was resolved by reverting the load balancer to its previous configuration and then carefully reapplying the intended updates, ensuring correct traffic routing.

## Corrective and Preventative Measures
- **Improvements**:
  - Review and enhance the change management process for critical infrastructure updates.
  - Implement additional automated checks to immediately flag misconfigurations in traffic routing.
  - Increase the frequency of scenario-based drills for the IT and cybersecurity teams to respond more effectively to diverse types of outages.
- **Specific Tasks**:
  1. **Conduct a full audit of the current load balancer configuration** to identify any other potential misconfigurations.
  2. **Update the automated monitoring system** to include specific checks for traffic routing discrepancies.
  3. **Revise the change management protocol** for critical updates, introducing additional layers of verification before deployment.
  4. **Schedule quarterly incident response drills** for the IT and cybersecurity teams, focusing on different outage scenarios.
  5. **Develop a comprehensive user communication plan** to more effectively inform users about ongoing issues and expected resolution times.
