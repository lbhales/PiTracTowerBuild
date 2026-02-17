# PiTrac Tower Build - Project Status

**Last Updated:** 2026-02-17

---

## Milestones

### Phase 1: Foundation (Current)
| Task | Status | Ralph Loop | Notes |
|------|--------|------------|-------|
| Create .claude.md | DONE | N/A (doc only) | All 7 mandatory rules defined |
| Create handoff.md | DONE | N/A (doc only) | Session continuity established |
| Create projectStatus.md | DONE | N/A (doc only) | This file |
| Create test framework | DONE | N/A (framework) | tests/ directory with smoke test |
| Initial commit and push | IN PROGRESS | N/A | First commit to branch |

### Phase 2: Pi 5 Base Setup (Upcoming)
| Task | Status | Ralph Loop | Notes |
|------|--------|------------|-------|
| Verify OS and dependencies | NOT STARTED | - | Check Pi 5 OS, packages |
| Configure camera dtoverlays | NOT STARTED | - | /boot/firmware/config.txt |
| Test camera detection | NOT STARTED | - | libcamera-hello --list-cameras |
| Install PiTrac dependencies | NOT STARTED | - | Build tools, libraries |

### Phase 3: PiTrac Software (Future)
| Task | Status | Ralph Loop | Notes |
|------|--------|------------|-------|
| Clone PiTrac repo | NOT STARTED | - | pitracLM/pitrac |
| Build PiTrac | NOT STARTED | - | Compile from source |
| Configure for one-camera design | NOT STARTED | - | Two IMX296 cameras |
| Camera calibration | NOT STARTED | - | Per PiTrac calibration docs |

### Phase 4: Integration & Testing (Future)
| Task | Status | Ralph Loop | Notes |
|------|--------|------------|-------|
| End-to-end capture test | NOT STARTED | - | Full pipeline test |
| Launch monitor validation | NOT STARTED | - | Ball tracking accuracy |

---

## Test Suite Status
| Test File | Tests | Passing | Last Run |
|-----------|-------|---------|----------|
| test_smoke.py | 3 | - | Not yet run |

---

## Decisions Made
| Date | Decision | Reason |
|------|----------|--------|
| 2026-02-17 | Use Ralph Loop (3-cycle TDD) | Owner mandate - quality first |
| 2026-02-17 | camelCase everywhere | Owner mandate - Smalltalk heritage |
| 2026-02-17 | Barney-style docs | Owner mandate - zero follow-up questions |
