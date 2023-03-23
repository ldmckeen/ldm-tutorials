import { TestBed } from '@angular/core/testing';

import { WordsmithService } from './wordsmith.service';

describe('WordsmithService', () => {
  let service: WordsmithService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(WordsmithService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
