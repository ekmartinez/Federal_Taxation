def print_dependency_report(result: dict) -> None:
    core = result["core"]
    qc = result["qualifying_child"]
    qr = result["qualifying_relative"]

    lines = ["Dependency Test:"]
    lines.append(f"    1) Citizen or resident Test:      {core['citizenship_residency_test']}")
    lines.append(f"    2) Joint return test:             {core['joint_return_test']}")

    if not core["passed"]:
        lines.append("                                     ------")
        lines.append(f"Core Requirements Result:            Failed")
        lines.append(f"Failed on:                            {', '.join(core['failed_tests'])}")
        lines.append("")
        lines.append(f"Dependent Status:                    {result['dependent_status']}")
        print("\n".join(lines))
        return

    lines.append("Qualifying Child Test:")
    lines.append(f"    3) Relationship test:             {qc['relationship_test']}")
    lines.append(f"    4) Age test:                      {qc['age_test']}")
    lines.append(f"    5) Residence test:                {qc['residence_test']}")
    lines.append(f"    6) Support test:                  {qc['support_test']}")
    lines.append("                                     ------")
    lines.append(f"Qualifying Child Test Result:         {'Passed' if qc['passed'] else 'Failed'}")
    if not qc["passed"]:
        lines.append(f"Failed on:                            {', '.join(qc['failed_tests'])}")

    if qr is not None:
        lines.append("")
        lines.append("Qualifying Relative Test:")
        lines.append(f"    7) Not a qualifying child test:   {qr['not_a_qualifying_child_test']}")
        lines.append(f"    8) Relationship/household test:   {qr['relationship_or_household_test']}")
        lines.append(f"    9) Gross income test:             {qr['gross_income_test']}")
        lines.append(f"    10) Support test:                 {qr['support_test']}")
        lines.append("                                     ------")
        lines.append(f"Qualifying Relative Test Result:      {'Passed' if qr['passed'] else 'Failed'}")
        if not qr["passed"]:
            lines.append(f"Failed on:                            {', '.join(qr['failed_tests'])}")

    lines.append("")
    lines.append(f"Dependent Status:                    {result['dependent_status']}")
    if result["reason"]:
        lines.append(f"Reason:                               {result['reason']}")

    print("\n".join(lines))
