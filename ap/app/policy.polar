# ==============================
# Role
# ==============================
allow(_, "read", _: ModelRole);

# ==============================
# User Role
# ==============================
allow(_, "read", _: ModelUserRole);

# ==============================
# School
# ==============================
allow(current_user, "read", _: ModelSchool) if
    "Administrator" in current_user.roles;

allow(current_user, "read", s: ModelSchool) if
    current_user.school_id = s.school_id;

# ==============================
# User
# ==============================
allow(current_user, "read", _: ModelUser) if
    "Administrator" in current_user.roles;

allow(current_user, "read", u: ModelUser) if
    current_user.school_id = u.school_id;

# ==============================
# Report Card
# ==============================
allow(current_user, "read", _: ModelReportCard) if
    "Administrator" in current_user.roles;

allow(current_user, "read", r: ModelReportCard) if
    current_user.user_id = r.user_id;

allow(current_user, "read", r: ModelReportCard) if
    "Teacher" in current_user.roles and
    current_user.user_id = r.user.teacher_id;

# ==============================
# Subject
# ==============================
allow(current_user, "read", _: ModelSubject) if
    "Administrator" in current_user.roles;

allow(current_user, "read", s: ModelSubject) if
    current_user.user_id = s.report_card.user_id;

allow(current_user, "read", s: ModelSubject) if
    "Teacher" in current_user.roles and
    current_user.user_id = s.report_card.user.teacher_id;

# ==============================
# Evaluation
# ==============================
allow(current_user, "read", _: ModelEvaluation) if
    "Administrator" in current_user.roles;

allow(current_user, "read", e: ModelEvaluation) if
    current_user.user_id = e.subject.report_card.user_id;

allow(current_user, "read", e: ModelEvaluation) if
    "Teacher" in current_user.roles and
    current_user.user_id = e.subject.report_card.user.teacher_id;

allow(current_user, "read", e: ModelEvaluation) if
    "Teacher" in current_user.roles and
    current_user.user_id = e.evaluated_by_id;
